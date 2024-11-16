from tkinter import *
import tkinter as tk
from tkinter import ttk
import time

class GUI ():
    """Graphical User Interface"""
    def __init__(self):
        self.window = None

    def set_window(self):
        """Establish The Window Configuration"""
        self.window.iconbitmap('assets/images/logo.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'DodgerBlue4')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)

    def set_label(self, text, font_size, relx, rely):
        """Establish A Label

        Args:
            text (str): Label Text
            font_size (int): Font Size
            relx (float): X Position
            rely (float): Y Position
        """
        label = Label(self.window, text = text, fg = 'goldenrod', bg = 'dodgerBlue4', font = ('Georgia', font_size, 'bold'))
        label.place(relx = relx, rely = rely, anchor = CENTER)

    def set_button(self, text, command, relx, rely):
        """Establish A Button

        Args:
            text (str): Button Text
            command (function): Button Command
            relx (float): X Position
            rely (float): Y Position
        """
        button = Button(self.window, text = text, fg = 'gold', bg = 'dodgerBlue3', font = ('Georgia', 12, 'bold'), command = command)
        button.place(relx = relx, rely = rely, width = 150, height = 40, anchor = CENTER)