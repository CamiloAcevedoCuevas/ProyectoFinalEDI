from tkinter import *

class GUI ():
    """Graphical User Interface"""
    def __init__(self, window):
        self.window = window

    def set_window(self, label_text, first_button_text, second_button_text, first_button_command, second_button_command):
        """Establish A New Window

        Args:
            label_text (str): Label Text
            first_button_text (str): First Button Text
            second_button_text (str): Second Button Text
            first_button_command (function): First Button Command
            second_button_command (function): Second Button Command
        """
        # Window Configuration
        self.window.iconbitmap('Assets/Logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'beige')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)
        # Window Components
        label = Label(self.window, text = label_text, fg = 'salmon', bg = 'beige', font = ('Algerian', 22))
        label.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        if second_button_text is None:
            x = 0.5
        else:
            x = 0.35
            button = Button(self.window, text = second_button_text, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = second_button_command)
            button.place(relx = 0.65, rely = 0.55, width = 150, height = 40, anchor = CENTER)
        button = Button(self.window, text = first_button_text, fg = 'salmon', bg = 'beige', font = ('Algerian', 12), command = first_button_command)
        button.place(relx = x, rely = 0.55, width = 150, height = 40, anchor = CENTER)