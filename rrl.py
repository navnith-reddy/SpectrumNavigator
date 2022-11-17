# ---------------------------------------------------------------
# ---- Register of Radiocommunication Licences (RRL) Library ----
# ---------------------------------------------------------------
# Australian Communications Media Authority
# Navnith Reddy, November 2022

# The RRL library provides support functions designed to assist
# data processing operations utilizing the ACMA's  publicly 
# available RRL database.

import pandas as pd
import geopandas as gpd
import requests
import zipfile
import os

# FUNCTION NAMING CONVENTION:
# -> 'get' functions download assets from ACMA website
# -> 'build' functions create assets based on downloaded assets
# -> 'read' functions are build functions that return variables

pd.options.mode.chained_assignment = None

def getRRL ():
    """Downloads Register of Radiocommuncation Licences"""
    
    # Create RRL folder if it doesn't exist
    if not os.path.exists("./RRL"):
        os.makedirs("./RRL")
    
    # Download RRL daily extract zip from ACMA website
    response = requests.get("https://web.acma.gov.au/rrl-updates/spectra_rrl.zip")
    open('RRL/spectra_rrl.zip', 'wb').write(response.content)
    
    # Extract zip file
    with zipfile.ZipFile("RRL/spectra_rrl.zip", 'r') as zip_ref:
        zip_ref.extractall("./RRL")
        
    return


def readSpecData ():
    """Creates dataframe and CSV file of Spectrum Licence information from RRL"""
    
    # From licence database, create dataset for spectrum licences
    licence = pd.read_csv('RRL/licence.csv')

    # Column tidy
    licence.drop(columns=[
        'SV_ID',
        'SS_ID',
        'DATE_ISSUED',
        'DATE_OF_EFFECT',
        'DATE_OF_EXPIRY',
        'STATUS',
        'STATUS_TEXT',
        'AP_ID',
        'AP_PRJ_IDENT',
        'SHIP_NAME',
        'BSL_NO'
        ], inplace=True)

    # Isolate and sort Spectrum Licence Entries
    specLicence = licence.loc[licence['LICENCE_TYPE_NAME'] == 'Spectrum']
    specLicence.reset_index(drop=True, inplace=True)
    specLicence = specLicence.astype({'LICENCE_NO':'int64', 'CLIENT_NO' : 'int64'})

    # Frequency dataset
    freq = pd.read_csv('RRL/auth_spectrum_freq.csv')
    freq = freq.astype({'LICENCE_NO':'int64'})

    # HCIS codes for frequency ranges
    area = pd.read_csv('RRL/auth_spectrum_area.csv')
    area = area.astype({'LICENCE_NO':'int64'})

    # Merge frequency dataset on spectrum licence dataset index
    SpecData = freq[freq['LICENCE_NO'].isin(specLicence['LICENCE_NO'])]
    bandNames = specLicence[['LICENCE_NO','LICENCE_CATEGORY_NAME', 'CLIENT_NO']]
    SpecData = pd.merge(SpecData, bandNames, how='left', on='LICENCE_NO')
    areaCodes = area[['AREA_CODE', 'AREA_DESCRIPTION']]
    SpecData = pd.merge(SpecData, areaCodes, how='left', on='AREA_CODE')

    # Add bandwidth values
    SpecData['UP_FREQUENCY_START'] = SpecData['UP_FREQUENCY_START'].fillna(0)
    SpecData['UP_FREQUENCY_END'] = SpecData['UP_FREQUENCY_END'].fillna(0)
    SpecData['LW_FREQUENCY_START'] = SpecData['LW_FREQUENCY_START'].fillna(0)
    SpecData['LW_FREQUENCY_END'] = SpecData['LW_FREQUENCY_END'].fillna(0)
    SpecData['LW_BW'] = SpecData['LW_FREQUENCY_END'] - SpecData['LW_FREQUENCY_START']
    SpecData['UP_BW'] = SpecData['UP_FREQUENCY_END'] - SpecData['UP_FREQUENCY_START']
    SpecData['BANDWIDTH'] = SpecData['LW_BW'] + SpecData['UP_BW']

    # Re-organize dataframe
    names = [
        'LICENCE_NO',
        'CLIENT_NO',
        'LW_FREQUENCY_START',
        'LW_FREQUENCY_END',
        'UP_FREQUENCY_START',
        'UP_FREQUENCY_END',
        'LW_BW',
        'UP_BW',
        'BANDWIDTH',
        'AREA_CODE',
        'AREA_NAME',
        'AREA_DESCRIPTION'
    ]
    
    SpecData = SpecData.reindex(columns=names)
    SpecData.reset_index(drop=True, inplace=False)
    SpecData.to_csv('SpectrumData.csv', index=False)
    
    return SpecData

def clientSearch(SpecData, clientIDs):
    """Generates dataframe containing spectrum licence information for input client numbers.

    Args:
        SpecData (Dataframe): RRL composite dataset of spectrum licence info.
        clientIDs (List): List of client numbers to be used as search keys.

    Returns:
        clientData (Dataframe): Dataframe containing spectrum licence info for specified client numbers.
    """
    
    # Parse inputs
    clientIDs = pd.Series(list(clientIDs.split(',')))
    clientIDs = clientIDs.astype('int64')
    
    # Input verification - // TO DO

    # Search spectrum dataset
    clientData = SpecData[SpecData['CLIENT_NO'].isin(clientIDs)]
    clientData.reset_index(drop=True, inplace=True)
    
    # No spectrum licences for client(s) number found (GUI)
    if clientData.empty:
        
        raise ValueError('No entries with provided client number')

    return clientData

def clientSummary (SpecData, clientIDs, clientData):
    
    # Generate client holding summary
    clientSummary = pd.DataFrame(clientIDs, columns=['CLIENT_NO'])
    holdingBandwidth = []

    for clientNum in list(clientIDs):
        
        holding = clientData[clientData['CLIENT_NO'] == clientNum]
        holdingBandwidth.append(holding['BANDWIDTH'].sum())

    clientSummary['TOTAL_BANDWIDTH_MHz'] = pd.Series(holdingBandwidth)/1000000
    
    # Fetch client name
    clients = pd.read_csv("RRL/client.csv")
    clients = clients[clients['CLIENT_NO'].isin(clientIDs)].reset_index()
    clientSummary = clientSummary.assign(LICENCEE=clients['LICENCEE'])
    
    return clientSummary

def buildgdf (clientData, asmg):
    """Takes clientData dataframe and generates a geodataframe containing HCIS polygons.

    Args:
        clientData (DataFrame): Client search results
        asmg (GeoDataFrame): Geodataframe of HCIS cells

    Returns:
        gdf (GeoDataFrame): Client search results with HCIS polygons
    """
    hcis = []

    for cells in clientData['AREA_DESCRIPTION']:
        cells = pd.Series(list(cells.split(', ')))
        clientArea = asmg[asmg['HCIS_ID'].isin(cells)]
        clientArea.reset_index(inplace=True)
        poly = clientArea['geometry']
        hcis.append(poly.unary_union)

    hcis = gpd.GeoSeries(hcis, crs='EPSG:4283')
    clientData['geometry'] = hcis
    gdf = gpd.GeoDataFrame(clientData)
    gdf.rename(columns = {
    "LW_FREQUENCY_START" : "LFREQ_START",
    "LW_FREQUENCY_END" : "LWFREQ_END",
    "UP_FREQUENCY_START" : "HIFREQ_START",
    "UP_FREQUENCY_END" : "HIFREQ_END",
    "UP_BW" : "HI_BW",
    "LICENCE_CATEGORY_NAME" : "BAND",
    "AREA_DESCRIPTION" : "HCIS"
    }, inplace = True)
    
    return gdf