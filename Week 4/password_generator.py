"""
    Name: password_generator_gui.py
    Author: Noel Onate
    Created: 9/11/25
    Purpose: GUI for generating random passwords.
"""

# Import tkinter libraries
from tkinter import *
from tkinter.ttk import *

# Import randint from random library
from random import randint

# Create strings with possible characters
WEAK = "abcdefghijklmnopqrstuvwxyz"
MEDIUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
STRONG = "1234567890-=!@#$%^&*()_+"

# Create class
class PasswordGeneratorGUI():

    # Create GUI
    def __init__(self):
        self.root = Tk()
        self.root.title("Random Password Generator")

        # Add icon to application
        self.icon = Image("photo", file="gear.gif")
        self.root.call('wm', 'iconphoto', self.root._w, self.icon)

        # Prevent window from resizing
        self.root.resizable(False, False)

        # Create the widgets and call mainloop to start program
        self.create_widgets()
        mainloop()

    # Method that creates a random password and inputs it into a text box
    def generate_password(self, strength):
        # Create variable for password
        self.password = ""

        # Check what strength of password user clicked
        # If its weak, only use the WEAK list for generator
        if strength == "weak":
            for self.i in range(10):
                # Generate a random number corresponding to length of WEAK list
                self.char_selection = randint(0, len(WEAK))
                
                # Add corresponding character from list to password minus 1 to prevent errors
                self.password += WEAK[self.char_selection - 1]
            
        # If its medium, use both WEAK and MEDIUM lists for generator
        elif strength == "medium":
            for self.i in range(10):
                # Generate a random number to pick either list randomly
                self.list_selection = randint(0, 1)

                # Decide which list was selected
                if self.list_selection == 0:
                    # If its 0, use the WEAK list to get a character
                    # Generate a random number corresponding to length of WEAK list
                    self.char_selection = randint(0, len(WEAK))

                    # Add corresponding character from list to password minus 1 to prevent errors
                    self.password += WEAK[self.char_selection - 1]

                elif self.list_selection == 1:
                    # If its 1, use the MEDIUM list to get a character
                    # Generate a random number corresponding to length of MEDIUM list
                    self.char_selection = randint(0, len(MEDIUM))

                    # Add corresponding character from list to password minus 1 to prevent errors
                    self.password += MEDIUM[self.char_selection - 1]
        
        # If its strong, use all three lists for generator
        elif strength == "strong":
            for self.i in range(10):
                # Generate a random number to pick a list randomly
                self.list_selection = randint(0, 2)

                # Decide which list was selected
                if self.list_selection == 0:
                    # If its 0, use the WEAK list to get a character
                    # Generate a random number corresponding to length of WEAK list
                    self.char_selection = randint(0, len(WEAK))

                    # Add corresponding character from list to password minus 1 to prevent errors
                    self.password += WEAK[self.char_selection - 1]

                elif self.list_selection == 1:
                    # If its 1, use the MEDIUM list to get a character
                    # Generate a random number corresponding to length of MEDIUM list
                    self.char_selection = randint(0, len(MEDIUM))

                    # Add corresponding character from list to password minus 1 to prevent errors
                    self.password += MEDIUM[self.char_selection - 1]
                
                elif self.list_selection == 2:
                    # If its 2, use the STRONG list to get a character
                    # Generate a random number corresponding to length of STRONG list
                    self.char_selection = randint(0, len(STRONG))

                    # Add corresponding character from list to password minus 1 to prevent errors
                    self.password += STRONG[self.char_selection - 1]
        
        # Set the text in output label to password generated
        self.lbl_password.config(text=self.password, anchor="center")

    # Method that copies the password to clipboard
    def copy_password(self):
        # Get the current string in the password output box
        self.password_copy = self.lbl_password.cget("text")

        # Clear anything currently in the clipboard
        self.root.clipboard_clear()

        # Add current password to clipboard
        self.root.clipboard_append(self.password_copy)

    # Method that creates GUI widgets
    def create_widgets(self):
        # Create frame to hold widgets
        self.main_frame = LabelFrame(self.root, relief=GROOVE)

        # Create widgets to display password and prompt text
        self.lbl_password = Label(self.main_frame, width=20, font=("Arial", 24), relief=GROOVE)
        self.lbl_prompt = Label(self.main_frame, text="Select Password Strength", relief=GROOVE)

        # Create buttons for GUI
        self.btn_weak = Button(self.main_frame, text="Weak", command=lambda: self.generate_password("weak"))
        self.btn_medium = Button(self.main_frame, text="Medium", command=lambda: self.generate_password("medium"))
        self.btn_strong = Button(self.main_frame, text="Strong", command=lambda: self.generate_password("strong"))
        self.btn_copy = Button(self.main_frame, text="Copy to Clipboard", command=self.copy_password)

        # Place all widgets in frame using grid method
        self.lbl_password.grid(row=0, column=1)
        self.lbl_prompt.grid(row=1, column=1)
        self.btn_weak.grid(row=2, column=0)
        self.btn_medium.grid(row=2, column=1)
        self.btn_strong.grid(row=2, column=2)
        self.btn_copy.grid(row=3, column=1)

        # Place frame in GUI using grid method
        self.main_frame.grid(row=0, column=0)

        # Set padding on frame and widgets
        self.main_frame.grid_configure(padx=20, pady=20)

        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

# Create object from class to run program
generator = PasswordGeneratorGUI()