from tkinter import *

class GUI ():
    """Graphical User Interface"""
    def __init__(self, window):
        self.window = window

    def set_window(self, text_label, text_btn1, text_btn2, command_1, command_2):
        """Establish A New Window

        Args:
            text_label (str): Label Text
            text_btn1 (str): First Button Text
            text_btn2 (str): Second Button Text
            command_1 (function): First Button Command
            command_2 (function): Second Button Command
        """
        # Window Configuration
        self.window.iconbitmap('Assets/Logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'beige')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)
        # Window Components
        label = Label(self.window, text = text_label, fg = 'salmon', bg = 'beige', font = ('Algerian', 22))
        label.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        if text_btn2 is None:
            x = 0.5
        else:
            x = 0.35
            button = Button(self.window, text = text_btn2, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = command_2)
            button.place(relx = 0.65, rely = 0.55, width = 150, height = 40, anchor = CENTER)
        button = Button(self.window, text = text_btn1, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = command_1)
        button.place(relx = x, rely = 0.55, width = 150, height = 40, anchor = CENTER)