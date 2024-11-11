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
    gui.set_window('El Poder De Un Click', 'Iniciar Partida', None, start, None)
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
        gui.set_window('Debes elegir si Javier invierte o no su dinero', 'Invertir', 'No Invertir', second_scene, third_scene)
        first_scene.mainloop()

        if scenes.scene == 2:
            scenes.get_scene(2)
            second_scene = Tk()
            def fourth_scene():
                scenes.scene = 4
                second_scene.destroy()
            def fifth_scene():
                scenes.scene = 5
                second_scene.destroy()
            gui = GUI(second_scene)
            gui.set_window('Debes elegir si Javier reporta a la policia o no', 'Reportar', 'No Reportar', fourth_scene, fifth_scene)
            second_scene.mainloop()

        elif scenes.scene == 3:
            scenes.get_scene(3)
            third_scene = Tk()
            def sixth_scene():
                scenes.scene = 6
                third_scene.destroy()
            def seventh_scene():
                scenes.scene = 7
                third_scene.destroy()
            gui = GUI(third_scene)
            gui.set_window('Debes elegir si Javier abre el correo o no', 'Abrir', 'No Abrir', sixth_scene, seventh_scene)
            third_scene.mainloop()

        if scenes.scene == 4:
            scenes.set_scene()

        elif scenes.scene == 5:
            scenes.get_scene(5)
            fifth_scene = Tk()
            def eighth_scene():
                scenes.scene = 8
                fifth_scene.destroy()
            def ninth_scene():
                scenes.scene = 9
                fifth_scene.destroy()
            gui = GUI(fifth_scene)
            gui.set_window('Debes elegir si Javier acepta la propuesta o no', 'Aceptar', 'No Aceptar', eighth_scene, ninth_scene)
            fifth_scene.mainloop()

            if scenes.scene == 8:
                scenes.set_scene()

            elif scenes.scene == 9:
                scenes.set_scene()

        elif scenes.scene == 6:
            scenes.set_scene()
        
        elif scenes.scene == 7:
            scenes.get_scene(7)
            seventh_scene = Tk()
            def tenth_scene():
                scenes.scene = 10
                seventh_scene.destroy()
            def eleventh_scene():
                scenes.scene = 11
                seventh_scene.destroy()
            gui = GUI(seventh_scene)
            gui.set_window('Decide se Javier instala el programa o no', 'Instalar', 'No Instalar', tenth_scene, eleventh_scene)
            seventh_scene.mainloop()

            if scenes.scene == 10:
                scenes.set_scene()

            elif scenes.scene == 11:
                scenes.set_scene()

if __name__ == '__main__':
    main()