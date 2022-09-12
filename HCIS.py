import geopandas as gpd
import pandas as pd
import requests
import os
import zipfile

def getASMG():
    """Downloads Australian Spectrum Map Grid shapefiles"""
    
    # Create ASMG folder if it doesn't exist
    if not os.path.exists("./ASMG"):
        os.mkdir("./ASMG")
    
    # Download ASMG shapefiles
    response = requests.get("https://channelfinder.acma.gov.au/webwr/spectrum-maps/ASMG_2012_GDA94.zip")
    open('ASMG/ASMG_2012_GDA94.zip', 'wb').write(response.content)
    
    # Extract zip file
    with zipfile.ZipFile("ASMG/ASMG_2012_GDA94.zip", 'r') as zip_ref:
        zip_ref.extractall("./ASMG")
    
    return

def buildASMG():
    """Returns geodataframe of ASMG for EVERY HCIS ID.

    Returns:
        asmg (geodataframe): geodataframe containing every HCIS cell.
    """
    
    l1 = gpd.read_file("ASMG/ASMG_2012_GDA94_L1.shp")
    l1.rename(columns={'HCI_Level1':'HCIS_ID'}, inplace=True)
    l1.drop(columns=['HCI_Level2', 'HCI_Level3', 'HCI_Level4'])

    l2 = gpd.read_file("ASMG/ASMG_2012_GDA94_L2.shp")
    l2.rename(columns={'HCI_Level2':'HCIS_ID'}, inplace=True)
    l2.drop(columns=['HCI_Level3', 'HCI_Level4'])

    l3 = gpd.read_file("ASMG/ASMG_2012_GDA94_L3.shp")
    l3.rename(columns={'HCI_Level3':'HCIS_ID'}, inplace=True)
    l3.drop(columns=['HCI_Level4'])

    l4 = gpd.read_file("ASMG/ASMG_2012_GDA94_L4.shp")
    l4.rename(columns={'HCI_Level4':'HCIS_ID'}, inplace=True)

    asmg = pd.concat([l1, l2, l3, l4])
    
    return asmg