import customtkinter as ct
import tkinter as tk

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