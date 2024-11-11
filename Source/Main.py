# El Poder De Un Click
# By Nebula Games®

import cv2
from tkinter import *
from Scenes import Scenes
from GUI import GUI

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
            gui.set_window('Debes elegir si Javier reporta a la policia o no', 'Reportar', 'No Reportar', scene4, scene5) # Reportar / No Reportar
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