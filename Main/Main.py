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
        """Return New Window"""
        self.window.iconbitmap('Assets/Logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'beige')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)
        label = Label(self.window, text = text_label, fg = 'salmon', bg = 'beige', font = ('Arial', 22))
        label.place(x = 300, y = 170)
        if text_btn2 is None:
            x = 430
        else:
            x = 310
        button = Button(self.window, text = text_btn1, fg = 'salmon', bg = 'beige', font = ('Arial', 12), command = command_1)
        button.place(x = x, y = 280, width = 150, height = 40)
        if text_btn2 is not None:
            button = Button(self.window, text = text_btn2, fg = 'salmon', bg = 'beige', font = ('Arial', 12), command = command_2)
            button.place(x = 530, y = 280, width = 150, height = 40)

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
                gui.get_window()
                gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                gui.get_button('Salir', 0, 20, 120, 40, exit)
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
                    gui.get_window()
                    gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                    gui.get_button('Salir', 0, 20, 120, 40, exit)
                def scene9(): # Scene 9
                    scene5.destroy()
                    scenes.get_scene(9)
                    scene9 = Tk()
                    def exit():
                        scene9.destroy()
                    gui = GUI(scene9)
                    gui.get_window()
                    gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                    gui.get_button('Salir', 0, 20, 120, 40, exit)
                gui = GUI(scene5)
                gui.get_window()
                gui.get_label('Decide si Javier acepta la propuesta o no', 370, 100, 24)
                gui.get_button('Aceptar', 310, 280, 150, 40, scene8) # Aceptar
                gui.get_button('No Aceptar', 530, 280, 150, 40, scene9) # No Aceptar
            gui = GUI(scene2)
            gui.get_window()
            gui.get_label('Debes elegir si Javier reporta la esta a la policia o no', 0, 0, 12)
            gui.get_button('Reportar', 310, 280, 150, 40, scene4) # Reportar
            gui.get_button('No Reportar', 530, 280, 150, 40, scene5) # No Reportar
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
                gui.get_window()
                gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                gui.get_button('Salir', 0, 20, 120, 40, exit)
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
                    gui.get_window()
                    gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                    gui.get_button('Salir', 0, 20, 120, 40, exit)
                def scene11(): # Scene 11
                    scene7.destroy()
                    scenes.get_scene(11)
                    scene11 = Tk()
                    def exit():
                        scene11.destroy()
                    gui = GUI(scene11)
                    gui.get_window()
                    gui.get_label('Gracias por jugar El Poder De Un Click', 370, 100, 24)
                    gui.get_button('Salir', 0, 20, 120, 40, exit)
                gui = GUI(scene7)
                gui.get_window()
                gui.get_label('Decide se Javier instala el programa o no', 370, 100, 24)
                gui.get_button('Instalar', 310, 280, 150, 40, scene10) # Instalar
                gui.get_button('No Instalar', 530, 280, 150, 40, scene11) # No Instalar
            gui = GUI(scene3)
            gui.get_window()
            gui.get_label('Debes elegir si Javier abre el correo o no', 0, 0, 12)
            gui.get_button('Abrir', 310, 280, 150, 40, scene6) # Abrir
            gui.get_button('No Abrir', 530, 280, 150, 40, scene7) # No Abrir
        gui = GUI(scene1)
        gui.get_window()
        gui.get_label('Debes elegir si Javier invierte o no su dinero', 260, 200, 18)
        gui.get_button('Invertir', 310, 280, 150, 40, scene2) # Invertir
        gui.get_button('No Invertir', 530, 280, 150, 40, scene3) # No Invertir
    gui = GUI(menu)
    gui.get_window()
    gui.get_label('El Poder De Un Click', 350, 150, 24)
    gui.get_button('Start', 430, 270, 120, 40, scene1)

    gui.window.mainloop() # Main Loop

if __name__ == '__main__':
    main()