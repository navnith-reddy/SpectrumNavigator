from re import search
import rrl
import pandas as pd

clientIDs = input("Please enter comma separated client IDs: ")
searchName = input("Please enter search name: ")
clientIDs = pd.Series(list(clientIDs.split(',')))

data = rrl.getSpecData()

clientData = data[data['CLIENT_NO'].isin(clientIDs)]
filename = searchName + '.csv'
clientData.to_csv(filename, index=False)