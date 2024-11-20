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

    def setLbl(self, txt, fs, rely):
        """Establish A Label

        Args:
            txt (str): Label Text
            fs (int): Font Size
            rely (float): Relative Y Position
        """
        label = Label(self.window, text = txt, fg = 'goldenrod', bg = 'gray2', font = ('Georgia', fs, 'bold'))
        label.place(relx = 0.5, rely = rely, anchor = CENTER)

    def setBtn(self, txt, command, relx, rely):
        """Establish A Button

        Args:
            txt (str): Button Text
            command (function): Button Command
            relx (float): Relative X Position
            rely (float): Relative Y Position
        """
        button = Button(self.window, text = txt, fg = 'goldenrod', bg = 'gray10', font = ('Georgia', 13, 'bold'), command = command)
        button.place(relx = relx, rely = rely, anchor = CENTER)

    def setImg(self, img, rely):
        """Establish An Image

        Args:
            img (str): Image
            rely (float): Relative Y Position
        """
        img = Label(self.window, image = img)
        img.place(relx = 0.5, rely = rely, anchor = CENTER)
        