# El Poder De Un Click
# By Nebula Games®

import cv2
from tkinter import *
from Scenes import Scenes
from GUI import GUI
import winsound

def main():
    scenes = Scenes()
    gui = GUI()

    for i in range(1, 4): # scenes buffering
        scene = cv2.VideoCapture(f'assets/videos/video{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk() # main menu
    gui.window = menu
    gui.set_window()
    image = PhotoImage(file="assets/images/background.png")
    label = ttk.Label(menu, image = image)
    label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    gui.set_label('El Poder De Un Click', 24, 0.5, 0.15)
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.set_button('Iniciar Partida', start, 0.4, 0.8)
    gui.set_button('Salir', exit, 0.6, 0.8)
    menu.mainloop()

    if scenes.scene == 'start':
        start = Tk()
        gui.window = start
        gui.set_window()
        #image = tk.PhotoImage(file="assets/images/javier.png")
        #label = ttk.Label(start, image=image)
        #label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        gui.set_label('Él es Javier. Javier es un excéntrico empresario de bienes raíces.\n Lleva una vida de ensueño en la ciudad de Nueva York y cuenta con innumerables inversiones exitosas. \nPero un día, todo eso cambió... Javier tiene un defecto, no sabe mucho sobre la seguridad en internet. \nTu deberás identificar si las acciones de Javier fueron las mejores o si aún tiene cosas que aprender.', 12, 0.5, 0.72)
        def scene1():
            scenes.scene = 1
            start.destroy()
        gui.set_button('Continuar', scene1, 0.5, 0.85)
        winsound.PlaySound('assets/audios/startaudio.wav', winsound.SND_ASYNC)
        start.mainloop()

        if scenes.scene == 1:
            scenes.get_scene(1)
            scene1 = Tk()
            gui.window = scene1
            gui.set_window()
            gui.
            
if __name__ == '__main__':
    main()
