import rrl
import HCIS
import os
import geopandas as gpd
import pandas as pd

# Rudimentary CLI
clientIDs = input("Please enter comma separated client IDs: ")
searchName = input("Please enter search name: ")

os.mkdir(searchName)

data = rrl.getSpecData()

# Perform search on RRL with client ID keys
clientData, clientSummary = rrl.clientSearch(data, clientIDs)
filename = searchName + '/data.csv'
summaryName = searchName + '/Summary.csv'

# Save search results as csv files
clientData.to_csv(filename, index=False)
clientSummary.to_csv(summaryName, index=False)

# --------- NEED TO FIX NAMING CONVENTIONS FOR COMPARISON-----------
# Convert search results to geodataframe and save as shapefiles
asmg = gpd.read_file('ASMG/asmg.shp')
gdf = rrl.buildgdf(clientData, asmg)
HCIS.preview(gdf, searchName + '/preview')
gdf.to_file(searchName+'/shapefile')