from tkinter import *

class GUI ():
    """Graphical User Interface"""
    def __init__(self, window):
        self.window = window

    def set_window(self, label_text, text1, text2, command1, command2):
        """Establish A New Window

        Args:
            label_text (str): Label Text
            text1 (str): First Button Text
            text2 (str): Second Button Text
            command1 (function): First Button Command
            command2 (function): Second Button Command
        """
        # Window Configuration
        self.window.iconbitmap('assets/logo/logo.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'DodgerBlue4')
        self.window.geometry('1280x720')
        self.window.resizable(False, False)
        # Window Components
        label = Label(self.window, text = label_text, fg = 'goldenrod', bg = 'DodgerBlue4', font = ('Georgia', 22, 'bold'))
        label.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        if text2 is None:
            x = 0.5
        else:
            x = 0.35
            button = Button(self.window, text = text2, fg = 'gold', bg = 'DodgerBlue3', font = ('Georgia', 12, 'bold'), command = command2)
            button.place(relx = 0.65, rely = 0.55, width = 150, height = 40, anchor = CENTER)
        button = Button(self.window, text = text1, fg = 'gold', bg = 'DodgerBlue3', font = ('Georgia', 12, 'bold'), command = command1)
        button.place(relx = x, rely = 0.55, width = 150, height = 40, anchor = CENTER)