import customtkinter as ct
import tkinter as tk

class App(ct.CTK):
    
    # Window dimensions as class attributes
    WIDTH = 780
    HEIGHT = 520
    
    def __init__(self):
        
        # super allows access to parent class members
        super().__init__()
        
        self.title("Spectrum Navigator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # Call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # ---------------- CREATE TWO FRAMES -------------------
        
        self.grid_columnconfigure

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