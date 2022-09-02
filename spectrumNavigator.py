import rrl
import HCIS
import pandas as pd

# Rudimentary CLI
clientIDs = input("Please enter comma separated client IDs: ")
searchName = input("Please enter search name: ")

data = rrl.getSpecData()

clientData, clientSummary = rrl.clientSearch(data, clientIDs)
filename = searchName + '.csv'
summaryName = searchName + 'Summary.csv'
clientData.to_csv(filename, index=False)
clientSummary.to_csv(summaryName, index=False)