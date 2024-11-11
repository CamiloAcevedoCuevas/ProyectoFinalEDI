# El Poder De Un Click
# By Nebula Games ®

import cv2 # Video Management
from tkinter import * # GUI
import winsound # Audio Management

class Scene:
    """A Game Scene"""
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None

class Scenes:
    """Game Scenes"""
    def __init__(self):
        self.head = None

    def add_scene(self, scene, index):
        """Add an scene

        Args:
            scene (VideoCapture): 
            index (int): Scene number
        """
        new_scene = Scene(scene, index)
        if self.head is None:
            self.head = new_scene
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_scene

    def get_scene(self, index):
        """Play an scene

        Args:
            index (int): Scene number
        """
        current = self.head
        while current is not None:
            if current.index == index:
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('', frame)
                        if cv2.waitKey(15) == 27:
                            break
                    else:
                        break
                break
            current = current.next
    
class GUI ():
    """Graphical User Interface"""
    def __init__(self, window):
        self.window = window

    def get_window(self):
        """Return New Window"""
        self.window.iconbitmap('Assets/Logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'white')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)

    def get_label(self, text, x, y, size):
        """Return New Label

        Args:
            text (str): Label Text
            x (int): X Position
            y (int): Y Position
            size (int): Font Size
        """
        label = Label(self.window, text = text, fg = 'black', bg = 'white', font = ('Arial', size))
        label.place(x = x, y = y)

    def get_button(self, text, x, y, width, height, command):
        button = Button(self.window, text = text, fg = 'black', bg = 'white', font = ('Arial', 12), command = command)
        button.place(x = x, y = y, width = width, height = height)

def main():
    scenes = Scenes()

    for i in range(1, 3): # Scenes Buffering
        scene = cv2.VideoCapture(f'Assets/scenes/scene{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk()
    gui = GUI(menu)
    def escena1():
        winsound.PlaySound('Assets/audios/aud1.wav', 0)
        scenes.get_scene(1)
        escena1 = Tk()
        gui = GUI(escena1)
        def escena2():
            winsound.PlaySound('Assets/audios/aud2.wav', 0)
            scenes.get_scene(2)
            escena2 = Tk()
            gui = GUI(escena2)
            def escena4():
                pass
            def escena5():
                pass
            gui.get_window()
            gui.get_label('Debes elegir si Javier reporta la esta a la policia o no', 0, 0, 12)
            gui.get_button('Reportar', 0, 20, 120, 40, escena4) # Reportar
            gui.get_button('No Reportar', 0, 60, 120, 40, escena5) # No Reportar
            escena1.destroy()
        def escena3():
            winsound.PlaySound('Assets/audios/aud3.wav', 0)
            scenes.get_scene(3)
            escena3 = Tk()
            gui = GUI(escena3)
            def escena6():
                pass
            def escena7():
                pass
            gui.get_window()
            gui.get_label('Debes elegir si Javier abre el correo o no', 0, 0, 12)
            gui.get_button('Abrir', 0, 20, 120, 40, escena6) # Abrir
            gui.get_button('No Abrir', 0, 60, 120, 40, escena7) # No Abrir
        gui.get_window()
        gui.get_label('Debes elegir si Javier invierte o no su dinero', 0, 0, 12)
        gui.get_button('Invertir', 0, 20, 120, 40, escena2)
        gui.get_button('No Invertir', 0, 60, 120, 40, escena3)
        menu.destroy()
    gui.get_window()
    gui.get_label('El Poder De Un Click', 370, 100, 24)
    gui.get_button('escena2', 0, 0, 120, 40, escena1)
    gui.window.mainloop() # Main Loop

if __name__ == '__main__':
    main()