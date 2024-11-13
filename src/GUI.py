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
        # self.window.iconbitmap('assets/logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'beige')
        self.window.geometry('1280x720')
        self.window.resizable(False, False)
        # Window Components
        label = Label(self.window, text = label_text, fg = 'salmon', bg = 'beige', font = ('Algerian', 22))
        label.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        if text2 is None:
            x = 0.5
        else:
            x = 0.35
            button = Button(self.window, text = text2, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = command2)
            button.place(relx = 0.65, rely = 0.55, width = 150, height = 40, anchor = CENTER)
        button = Button(self.window, text = text1, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = command1)
        button.place(relx = x, rely = 0.55, width = 150, height = 40, anchor = CENTER)
