# El Poder De Un Click
# By Nebula Games®

import cv2
from tkinter import *
from Scenes import Scenes
from GUI import GUI
from tkinter import ttk

def main():
    scenes = Scenes()
    gui = GUI()

    for i in range(1, 4): # scenes buffering
        scene = cv2.VideoCapture(f'assets/videos/video{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk() # main menu
    gui.window = menu
    gui.set_window()
    image = PhotoImage(file="assets/images/newyork.png")
    label = ttk.Label(menu, image=image)
    label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    gui.set_label('El Poder De Un Click', 22, 0.5, 0.35)
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.set_button('Iniciar Partida', start, 0.35, 0.55)
    gui.set_button('Salir', exit, 0.65, 0.55)
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
        start.mainloop()

        if scenes.scene == 1:
            print("xd")


    # if scenes.scene == 1:
    #     scenes.get_scene(1) # charges scene 1
    #     scene1 = Tk()
    #     def scene2():
    #         scenes.scene = 2
    #         scene1.destroy()
    #     def scene3():
    #         scenes.scene = 3
    #         scene1.destroy()
    #     gui = GUI(scene1)
    #     gui.set_window('Invertir Dinero', 'Si', 'No', scene2, scene3)
    #     scene1.mainloop()

    #     if scenes.scene == 2:
    #         scenes.get_scene(2) # charges scene 2
    #         scene2 = Tk()
    #         def scene4():
    #             scenes.scene = 4
    #             scene2.destroy()
    #             scenes.set_exit_scene() # charges scene 4
    #         def scene5():
    #             scenes.scene = 5
    #             scene2.destroy()
    #         gui = GUI(scene2)
    #         gui.set_window('Llamar a la policía', 'Si', 'No', scene4, scene5)
    #         scene2.mainloop()

    #     elif scenes.scene == 3:
    #         scenes.get_scene(3) # charges scene 3
    #         scene3 = Tk()
    #         def scene6():
    #             scenes.scene = 6
    #             scene3.destroy()
    #             scenes.set_exit_scene() # charges scene 6
    #         def scene7():
    #             scenes.scene = 7
    #             scene3.destroy()
    #         gui = GUI(scene3)
    #         gui.set_window('Abrir el correo', 'Si', 'No', scene6, scene7)
    #         scene3.mainloop()

    #     if scenes.scene == 5:
    #         scenes.get_scene(5) # charges scene 5
    #         scene5 = Tk()
    #         def scene8():
    #             scenes.scene = 8
    #             scene5.destroy()
    #             scenes.set_exit_scene() # charges scene 8
    #         def scene9():
    #             scenes.scene = 9
    #             scene5.destroy()
    #             scenes.set_exit_scene() # charges scene 9
    #         gui = GUI(scene5)
    #         gui.set_window('Aceptar la propuesta', 'Si', 'No', scene8, scene9)
    #         scene5.mainloop()

    #     elif scenes.scene == 7:
    #         scenes.get_scene(7)
    #         scene7 = Tk()
    #         def scene10():
    #             scenes.scene = 10
    #             scene7.destroy()
    #             scenes.set_exit_scene() # charges scene 10
    #         def scene11():
    #             scenes.scene = 11
    #             scene7.destroy()
    #             scenes.set_exit_scene() # charges scene 11
    #         gui = GUI(scene7)
    #         gui.set_window('Instalar el programa', 'Si', 'No', scene10, scene11)
    #         scene7.mainloop()

if __name__ == '__main__':
    main()