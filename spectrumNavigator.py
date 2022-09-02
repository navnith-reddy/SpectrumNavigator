from re import search
import rrl
import pandas as pd

# Rudimentary CLI
clientIDs = input("Please enter comma separated client IDs: ")
searchName = input("Please enter search name: ")
clientIDs = pd.Series(list(clientIDs.split(',')))

data = rrl.getSpecData()

clientData = rrl.clientSearch(data, clientIDs)
filename = searchName + '.csv'
clientData.to_csv(filename, index=False)