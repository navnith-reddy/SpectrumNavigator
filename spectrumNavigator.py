import rrl
import HCIS
import os
import gui
import geopandas as gpd
import pandas as pd
import customtkinter as ct
import tkinter as tk

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

ct.set_appearance_mode("light")
ct.set_default_color_theme("green")

app = ct.CTk()
app.geometry("600x400")

#label = ct.CTkLabel(master=app, text='INITIALIZING...')
#label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# INITIALISE
#data = rrl.readSpecData()
#asmg = HCIS.buildASMG()

mainFrame = ct.CTkFrame(master=app, 
                    width=200,
                    height=200,
                    corner_radius=20)

licButton = ct.CTkButton(mainFrame, text="Licence Extract", command=gui.doLicExtract)
licButton.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

cliButton = ct.CTkButton(mainFrame, text="Client Extract", command=gui.doCliExtract)
cliButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

hcisButton = ct.CTkButton(mainFrame, text="HCIS Conversion", command=gui.doPoly2HCIS)
hcisButton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

mainFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()