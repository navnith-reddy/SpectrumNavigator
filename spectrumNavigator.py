import rrl
import HCIS
import os
import geopandas as gpd
import pandas as pd
import customtkinter as ct

def clientExtract (clientIDs, data, asmg):

    # Perform search on RRL with client ID keys
    clientData, clientSummary = rrl.clientSearch(data, clientIDs)
    
    # Create a geodataframe from clientData
    gdf = rrl.buildgdf(clientIDs, asmg)
    
    return gdf,

def licenceExtract (licenceNums):
    
    return

def holdingsSummary (clientNums):
    
    return

# INITIALISE
#data = rrl.readSpecData()
#asmg = HCIS.buildASMG()

import tkinter as tk

ct.set_appearance_mode("light")
ct.set_default_color_theme("green")

app = ct.CTk()
app.geometry("1200x400")


def doLicExtract():
    dialog = ct.CTkInputDialog(master=None, text="Type in a Licence number:", title="Test")
    print("Licence Number:", dialog.get_input())
    
def doCliExtract():
    dialog = ct.CTkInputDialog(master=None, text="Type in a Client ID:", title="Test")
    print("Client ID:", dialog.get_input())
    
def doPoly2HCIS():
    dialog = ct.CTkInputDialog(master=None, text="Type in a Client ID:", title="Test")
    print("Client ID:", dialog.get_input())

def doHoldings():
    dialog = ct.CTkInputDialog(master=None, text="Type in a Client ID:", title="Test")
    print("Client ID:", dialog.get_input())



licButton = ct.CTkButton(app, text="Licence Extract", command=doLicExtract)
licButton.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

cliButton = ct.CTkButton(app, text="Client Extract", command=doCliExtract)
cliButton.place(relx=0.50, rely=0.5, anchor=tk.CENTER)

cliButton = ct.CTkButton(app, text="HCIS Conversion", command=doCliExtract)
cliButton.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

app.mainloop()