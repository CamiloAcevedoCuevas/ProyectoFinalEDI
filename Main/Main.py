# El Poder De Un Click
# By Nebula Games®

import cv2 # Video Management
from tkinter import * # GUI
import winsound # Audio Management

class Scene:
    """Represents A Game Scene"""
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
        winsound.PlaySound(f'Assets/Audios/Audio{index}', winsound.SND_ASYNC)
        current = self.head
        while current is not None:
            if current.index == index:
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('', frame)
                        cv2.waitKey(15)
                    else:
                        break
                break
            current = current.next
    
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
        label = Label(self.window, text = text_label, fg = 'salmon', bg = 'beige', font = ('Arial', 22))
        label.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        if text_btn2 is None:
            x = 0.5
            text_btn2 = text_btn1
        else:
            x = 0.35
            button = Button(self.window, text = text_btn2, fg = 'salmon', bg = 'beige', font = ('Arial', 12), command = command_2)
            button.place(relx = 0.65, rely = 0.55, width = 150, height = 40, anchor = CENTER)
        button = Button(self.window, text = text_btn1, fg = 'salmon', bg = 'beige', font = ('Arial', 12), command = command_1)
        button.place(relx = x, rely = 0.55, width = 150, height = 40, anchor = CENTER)

def main():
    scenes = Scenes()

    for i in range(1, 11): # Scenes Buffering
        scene = cv2.VideoCapture(f'Assets/Scenes/Scene{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk()
    def scene1(): # Scene 1
        menu.destroy()
        scenes.get_scene(1)
        scene1 = Tk()
        def scene2(): # Scene 2
            scene1.destroy()
            scenes.get_scene(2)
            scene2 = Tk()
            gui = GUI(scene2)
            def scene4(): # Scene 4
                scene2.destroy()
                scenes.get_scene(4)
                scene4 = Tk()
                def exit():
                    scene4.destroy()
                gui = GUI(scene4)
                gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
            def scene5(): # Scene 5
                scene2.destroy()
                scenes.get_scene(5)
                scene5 = Tk()
                def scene8(): # Scene 8
                    scene5.destroy()
                    scenes.get_scene(8)
                    scene8 = Tk()
                    def exit():
                        scene8.destroy()
                    gui = GUI(scene8)
                    gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
                def scene9(): # Scene 9
                    scene5.destroy()
                    scenes.get_scene(9)
                    scene9 = Tk()
                    def exit():
                        scene9.destroy()
                    gui = GUI(scene9)
                    gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
                gui = GUI(scene5)
                gui.set_window('Debes elegir si Javier acepta la propuesta o no', 'Aceptar', 'No Aceptar', scene8, scene9) # Aceptar / No Aceptar
            gui = GUI(scene2)
            gui.set_window('Debes elegir si Javier reporta la esta a la policia o no', 'Reportar', 'No Reportar', scene4, scene5) # Reportar / No Reportar
        def scene3(): # Scene 3
            scene1.destroy()
            scenes.get_scene(3)
            scene3 = Tk()
            def scene6(): # Scene 6
                scene3.destroy()
                scenes.get_scene(6)
                scene6 = Tk()
                def exit():
                    scene6.destroy()
                gui = GUI(scene6)
                gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
            def scene7(): # Scene 7
                scene3.destroy()
                scenes.get_scene(7)
                scene7 = Tk()
                def scene10(): # Scene 10
                    scene7.destroy()
                    scenes.get_scene(10)
                    scene10 = Tk()
                    def exit():
                        scene10.destroy()
                    gui = GUI(scene10)
                    gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
                def scene11(): # Scene 11
                    scene7.destroy()
                    scenes.get_scene(11)
                    scene11 = Tk()
                    def exit():
                        scene11.destroy()
                    gui = GUI(scene11)
                    gui.set_window('Gracias por jugar El Poder De Un Click', 'Salir', None, exit, None)
                gui = GUI(scene7)
                gui.set_window('Decide se Javier instala el programa o no', 'Instalar', 'No Instalar', scene10, scene11) # Instalar / No Instalar
            gui = GUI(scene3)
            gui.set_window('Debes elegir si Javier abre el correo o no', 'Abrir', 'No Abrir', scene6, scene7) # Abrir / No Abrir
        gui = GUI(scene1)
        gui.set_window('Debes elegir si Javier invierte o no su dinero', 'Invertir', 'No Invertir', scene2, scene3) # Invertir / No Invertir
    gui = GUI(menu)
    gui.set_window('El Poder De Un Click', 'Start', None, scene1, None)

    gui.window.mainloop() # Main Loop

if __name__ == '__main__':
    main()