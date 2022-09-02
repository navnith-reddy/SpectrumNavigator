import geopandas as gpd
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