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