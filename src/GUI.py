from tkinter import *

class GUI ():
    """Graphical User Interface Class."""
    def __init__(self):
        self.window = None

    def set_window(self):
        """Establish A Window."""
        self.window.iconbitmap('assets/images/logo.ico')
        self.window.title('El Poder De Un Click')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)

    def set_label(self, text, font_size, relx, rely, fg, bg):
        """Establish A Label

        Args:
            text (str): Label Text
            font_size (int): Font Size
            relx (float): X Position
            rely (float): Y Position
            fg (str): Label Foreground Color
            bg (str): Label Background Color
        """
        label = Label(self.window, text = text, fg = fg, bg = bg, font = ('Georgia', font_size, 'bold'))
        label.place(relx = relx, rely = rely, anchor = CENTER)

    def set_button(self, text, command, relx, rely, width, height, fg, bg):
        """Establish A Button

        Args:
            text (str): Button Text
            command (function): Button Command
            relx (float): X Position
            rely (float): Y Position
            width (int): Width Size
            height (int): Height Size
            fg (str): Button Foreground Color
            bg (str): Button Background Color
        """
        button = Button(self.window, text = text, fg = fg, bg = bg, font = ('Georgia', 12, 'bold'), command = command)
        button.place(relx = relx, rely = rely, width = width, height = height, anchor = CENTER)