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

    menu = Tk() # Main Menu
    def start():
        scenes.scene = 1
        menu.destroy()
    gui = GUI(menu)
    gui.set_window('El Poder De Un Click', 'Nueva Partida', None, start, None)
    menu.mainloop()

    if scenes.scene == 1:
        scenes.get_scene(1)
        first_scene = Tk()
        def second_scene():
            scenes.scene = 2
            first_scene.destroy()
        def third_scene():
            scenes.scene = 3
            first_scene.destroy()
        gui = GUI(first_scene)
        gui.set_window('Invertir Dinero', 'Si', 'No', second_scene, third_scene)
        first_scene.mainloop()

        if scenes.scene == 2:
            scenes.get_scene(2)
            second_scene = Tk()
            def fourth_scene():
                scenes.scene = 4
                second_scene.destroy()
                scenes.set_exit_scene()
            def fifth_scene():
                scenes.scene = 5
                second_scene.destroy()
            gui = GUI(second_scene)
            gui.set_window('Llamar a la policía', 'Si', 'No', fourth_scene, fifth_scene)
            second_scene.mainloop()

        elif scenes.scene == 3:
            scenes.get_scene(3)
            third_scene = Tk()
            def sixth_scene():
                scenes.scene = 6
                third_scene.destroy()
                scenes.set_exit_scene()
            def seventh_scene():
                scenes.scene = 7
                third_scene.destroy()
            gui = GUI(third_scene)
            gui.set_window('Abrir el correo', 'Si', 'No', sixth_scene, seventh_scene)
            third_scene.mainloop()

        if scenes.scene == 5:
            scenes.get_scene(5)
            fifth_scene = Tk()
            def eighth_scene():
                scenes.scene = 8
                fifth_scene.destroy()
                scenes.set_exit_scene()
            def ninth_scene():
                scenes.scene = 9
                fifth_scene.destroy()
                scenes.set_exit_scene()
            gui = GUI(fifth_scene)
            gui.set_window('Aceptar la propuesta', 'Si', 'No', eighth_scene, ninth_scene)
            fifth_scene.mainloop()

        elif scenes.scene == 7:
            scenes.get_scene(7)
            seventh_scene = Tk()
            def tenth_scene():
                scenes.scene = 10
                seventh_scene.destroy()
                scenes.set_exit_scene()
            def eleventh_scene():
                scenes.scene = 11
                seventh_scene.destroy()
                scenes.set_exit_scene()
            gui = GUI(seventh_scene)
            gui.set_window('Instalar el programa', 'Si', 'No', tenth_scene, eleventh_scene)
            seventh_scene.mainloop()

if __name__ == '__main__':
    main()