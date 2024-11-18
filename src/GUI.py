from tkinter import *

class GUI ():
    """Graphical User Interface Class."""
    def __init__(self):
        self.window = None

    def setWindow(self):
        """Establish A Window."""
        self.window.iconbitmap('assets/images/logo.ico')
        self.window.title('El Poder De Un Click')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)

    def setLbl(self, txt, fs, relx, rely, fg, bg):
        """Establish A Label

        Args:
            txt (str): Label Text
            fs (int): Font Size
            relx (float): Relative X Position
            rely (float): Relative Y Position
            fg (str): Label Foreground Color
            bg (str): Label Background Color
        """
        label = Label(self.window, text = txt, fg = fg, bg = bg, font = ('Georgia', fs, 'bold'))
        label.place(relx = relx, rely = rely, anchor = CENTER)

    def setBtn(self, txt, command, relx, rely, w, h, fg, bg):
        """Establish A Button

        Args:
            txt (str): Button Text
            command (function): Button Command
            relx (float): Relative X Position
            rely (float): Relative Y Position
            w (int): Width
            h (int): Height
            fg (str): Button Foreground Color
            bg (str): Button Background Color
        """
        button = Button(self.window, text = txt, fg = fg, bg = bg, font = ('Georgia', 12, 'bold'), command = command)
        button.place(relx = relx, rely = rely, width = w, height = h, anchor = CENTER)

    def setImg(self, img, relx, rely):
        """Establish An Image

        Args:
            img (str): Image
            relx (float): Relative X Position
            rely (float): Relative Y Position
        """
        img = Label(self.window, image = img)
        img.place(relx = relx, rely = rely, anchor = CENTER)