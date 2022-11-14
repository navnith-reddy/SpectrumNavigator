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
    
    # /////////////////////// POTENTIAL MEMORY LEAK //////////////////////
    def landingPage (self):
        
        # --------------------- CREATE TWO FRAMES ------------------------
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        self.panel = ct.CTkFrame(master=self, width=180, corner_radius=0)
        self.panel.grid(row=0, column=0, sticky="nswe")
        
        self.right = ct.CTkFrame(master=self, width=360, corner_radius=10)
        self.right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
        # -------------------------- PANEL -------------------------------
        
        # Setup Panel Grid
        self.panel.grid_columnconfigure(0, weight=1)
        self.panel.grid_rowconfigure(0, weight=1)
        self.panel.grid_rowconfigure(1, weight=1)
        self.panel.grid_rowconfigure(2, weight=1)
        self.panel.grid_rowconfigure(3, weight=1)
       
        # Setup Panel Prompt
        prompt = ct.CTkLabel(master=self.panel,
                            text="Select operation:",
                            text_font=('Arial', -16))
        prompt.grid(row=0, column=0, padx = 1, pady = 1)       
       
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
        
        # Program title in right frame
        mainTitle =  ct.CTkLabel(master=self.right,
                                text="Spectrum Navigator",
                                text_font=('Arial', -42))
        mainTitle.grid(row=0, column=0, padx = 1, pady = 1)
        
        # Read logo image
        logo = ImageTk.PhotoImage(Image.open('./assets/ACMA_logo.png'))
        logoBtn = ct.CTkButton(master=self.right,
                                fg_color=None,
                                hover=False,
                                image=logo, 
                                text="")
        logoBtn.grid(row=1, column= 0)
        
        # Fine text
        fineText =  ct.CTkLabel(master=self.right,
                            text="ACMA Spectrum Navigator - Version 0.1      Last Updated: Nov 2022",
                            text_font=('Arial', -10))
        fineText.grid(row=2, column=0, padx = 1, pady = 1, sticky='s')
        
    def blank (self):
        
        # Clear Widgets
        self.panel.destroy()
        self.right.destroy()
        
        # Recreate two frames
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        self.panel = ct.CTkFrame(master=self, width=180, corner_radius=0)
        self.panel.grid(row=0, column=0, sticky="nswe")
        
        self.right = ct.CTkFrame(master=self, width=360, corner_radius=10)
        self.right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    
    def back(self):
        
        # Clear Widgets
        self.panel.destroy()
        self.right.destroy()
        
        # Go back to landing page
        self.landingPage()
        
        print("Back Button Pressed")
    
    # Open Licence Extract 
    def doLicExtract(self):
        
        # Clear window
        self.blank()
        
        # -------------------------- PANEL -------------------------------
        
        # Setup panel grid
        self.panel.grid_columnconfigure(0, weight=1)
        self.panel.grid_rowconfigure(2, weight=2)
        self.panel.grid_rowconfigure(9, weight=1)
        
        # Licence Number Entry
        LicNumPrompt = ct.CTkLabel(master=self.panel,
                                  text="Licence Number(s):",
                                  text_font=('Arial', -16))
        LicNumPrompt.grid(row=1, column=0)
        
        LicNumEntry = ct.CTkEntry(master=self.panel,
                                  placeholder_text="Enter a single licence number \n or comma separated licence numbers",
                                  border_width=2,
                                  corner_radius=10)
        LicNumEntry.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
        
        LicNumEntry = ct.CTkEntry(master=self.panel,
                                  placeholder_text="Enter a single licence number \n or comma separated licence numbers",
                                  border_width=2,
                                  corner_radius=10)
        LicNumEntry.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
        
        # Back Button
        backBtn = ct.CTkButton(master=self.panel, 
                                text="Back", 
                                command=self.back)
        backBtn.grid(row=8, column=0, padx = 30, pady = 30, sticky='nswe')
        
        print("Licence Number button pressed")
    
    def doCliExtract(self):
        
        # Clear window
        self.blank()
        
        print("Client ID button pressed")
    
    def doPoly2HCIS(self):
        
        # Clear window
        self.blank()
        
        print("HCIS Conversion button pressed")

    def doHoldings(self):
        
        # Clear window
        self.blank()
        
        print("Holdings button pressed")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()