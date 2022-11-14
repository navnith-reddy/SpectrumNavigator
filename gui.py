import customtkinter as ct
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(ct.CTk):
    
    # Window dimensions as class attributes
    WIDTH = 780
    HEIGHT = 520
    
    def __init__(self):
        
        # super allows access to parent class members
        super().__init__()
        
        self.title("Spectrum Navigator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        ct.set_appearance_mode("light")
        ct.set_default_color_theme("green")
        # Call .on_closing() when app gets closed
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.landingPage()
    
    def landingPage (self):
        
        # --------------------- CREATE TWO FRAMES ------------------------
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        self.panel = ct.CTkFrame(master=self, width=180, corner_radius=5)
        self.panel.grid(row=0, column=0, sticky="nswe", padx=5, pady=10)
        
        self.right = ct.CTkFrame(master=self, width=360, corner_radius=5)
        self.right.grid(row=0, column=1, sticky="nswe", padx=5, pady=10)
        
        # -------------------------- PANEL -------------------------------
        
        # Setup Panel Grid
        self.panel.grid_columnconfigure(0, weight=1)
        self.panel.grid_rowconfigure(0, weight=1)
        self.panel.grid_rowconfigure(1, weight=1)
        self.panel.grid_rowconfigure(2, weight=1)
        self.panel.grid_rowconfigure(3, weight=1)
       
        # Setup Panel Prompt
        self.prompt = ct.CTkLabel(master=self.panel,
                            text="Select operation:",
                            text_font=('Arial', -16))
        self.prompt.grid(row=0, column=0, padx = 1, pady = 1)       
       
        # Setup Panel buttons 
        licButton = ct.CTkButton(master=self.panel, 
                                text="Licence Extract", 
                                command=self.doLicExtract)
        licButton.grid(row=1, column=0, padx = 30, pady = 30, sticky='nswe')

        cliButton = ct.CTkButton(master=self.panel, 
                                text="Client Extract", 
                                command=self.doCliExtract)
        cliButton.grid(row=2, column=0, padx = 30, pady = 30, sticky='nswe')

        hcisButton = ct.CTkButton(master=self.panel, 
                                text="HCIS Conversion", 
                                command=self.doPoly2HCIS)
        hcisButton.grid(row=3, column=0, padx = 30, pady = 30, sticky='nswe')
        
        # -------------------------- RIGHT FRAME -------------------------
        
        # Setup Grid
        self.right.grid_columnconfigure(0, weight=1)
        self.right.grid_rowconfigure(0, weight=1)
        self.right.grid_rowconfigure(1, weight=2)
        self.right.grid_rowconfigure(2, weight=1)
        
        
        
        self.mainTitle =  ct.CTkLabel(master=self.right,
                            text="Spectrum Navigator",
                            text_font=('Arial', -42))
        self.mainTitle.grid(row=0, column=0, padx = 1, pady = 1)
        
        # Read logo image
        self.logo = ImageTk.PhotoImage(Image.open('./assets/ACMA_logo.png'))
        self.logo = ct.CTkButton(master=self.right,
                                fg_color=None,
                                hover=False,
                                image=self.logo, 
                                text="")
        self.logo.grid(row=1, column= 0)
        
        # Fine text
        self.fineText =  ct.CTkLabel(master=self.right,
                            text="ACMA Spectrum Navigator - Version 0.1      Last Updated: Nov 2022",
                            text_font=('Arial', -10))
        self.fineText.grid(row=2, column=0, padx = 1, pady = 1, sticky='s')
        

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
    
if __name__ == "__main__":
    app = App()
    app.mainloop()