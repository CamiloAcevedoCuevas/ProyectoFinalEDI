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
    gui.set_window(None)
    image = PhotoImage(file = 'assets/images/backgrounds/mainmenu.png')
    background = Label(menu, image = image)
    background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    gui.set_label('El Poder De Un Click', 24, 0.5, 0.15, 'goldenrod', 'dodgerBlue4')
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.set_button('Iniciar Partida', start, 0.4, 0.8, 150, 40, 'goldenrod', 'dodgerBlue4')
    gui.set_button('Salir', exit, 0.6, 0.8, 150, 40, 'goldenrod', 'dodgerBlue4')
    menu.mainloop()

    if scenes.scene == 'start':
        start = Tk()
        gui.window = start
        gui.set_window('dodgerBlue4')
        #image = tk.PhotoImage(file = "assets/images/javier.png")
        #label = ttk.Label(start, image = image)
        #label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        gui.set_label('Él es Javier. Javier es un excéntrico empresario de bienes raíces.\n Lleva una vida de ensueño en la ciudad de Nueva York y cuenta con innumerables inversiones exitosas. \nPero un día, todo eso cambió... Javier tiene un defecto, no sabe mucho sobre la seguridad en internet. \nTu deberás identificar si las acciones de Javier fueron las mejores o si aún tiene cosas que aprender.', 12, 0.5, 0.85, 'goldenrod', 'dodgerBlue4')
        winsound.PlaySound('assets/audios/javier.wav', winsound.SND_ASYNC) # Reproduce el audio donde se presenta a Javier.
        def scene1():
            scenes.scene = 1
            start.destroy()
        start.after(5000, scene1)
        start.mainloop()

        if scenes.scene == 1:
            scenes.play_scene(1) # Reproduce la escena donde Javier se conecta al wifi.
            scene1 = Tk()
            gui.window = scene1
            gui.set_window(None)
            image = PhotoImage(file = 'assets/images/backgrounds/scene1.png')
            background = Label(scene1, image = image)
            background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            gui.set_label('¿Usted haría lo mismo que Javier?', 22, 0.5, 0.2, 'goldenrod', 'gray2')
            def scene2():
                scenes.scene = 2
                scene1.destroy()
            def scene3():
                scenes.scene = 3
                scene1.destroy()
            gui.set_button('SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo', scene2, 0.5, 0.5, 930, 40, 'goldenrod', 'gray10')
            gui.set_button('No, es muy sospechoso', scene3, 0.5, 0.65, 250, 40, 'goldenrod', 'gray10')
            scene1.mainloop()

            while True:
                if scenes.scene == 2:
                    scenes.scene = None
                    scenes.play_scene(2) # Muestra la secuencia donde Javier recuerda la conversación con su primo Juan.
                    scene2 = Tk()
                    gui.window = scene2
                    gui.set_window('gray72')
                    gui.set_label('¿Está seguro de que fue lo correcto?', 22, 0.5, 0.2, 'gray16', 'gray90')
                    def reset():
                        scenes.scene = 2
                        scene2.destroy()
                    def scene3():
                        scenes.scene = 3
                        scene2.destroy()
                    gui.set_button('SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo', reset, 0.5, 0.5, 930, 40, 'gray16', 'gray90')
                    gui.set_button('No, es muy sospechoso', scene3, 0.5, 0.65, 250, 40, 'gray16', 'gray90')
                    scene2.mainloop()
                else:
                    break

            if scenes.scene == 3:
                scenes.play_scene(3) # Muestra la secuencia donde se felicita al jugador por haber identificado la actividad sospechosa.
                winsound.PlaySound('assets/audios/transicion.wav', 0) # Reproduce el audio donde explica que las cookies de Javier fueron robadas.
                scene3 = Tk()
                gui.window = scene3
                gui.set_window('dodgerBlue4')
                def cookies():
                    gui.set_label('Las cookies son pequeños archivos de texto que los sitios web guardan en tu dispositivo cuando los visitas.\n Sirven para almacenar información sobre tu actividad en línea', 12, 0.5, 0.72, 'goldenrod', 'dodgerBlue4')
                    winsound.PlaySound('assets/audios/cookies.wav', 0) # Reproduce el audio con la explicación de las cookies.
                    scenes.scene = 4
                    scene3.destroy()
                gui.set_button('¿Cookies?', cookies, 0.5, 0.5, 150, 40, 'goldenrod', 'dodgerBlue4')
                scene3.mainloop()

            if scenes.scene == 4:
                scenes.play_scene(4) # Muestra la escena donde Javier encuentra Axi.
                scene4 = Tk()
                gui.window = scene4
                gui.set_window('dodgerBlue4')
                gui.set_label('Hay algo extraño en esta página, identifíquelo:', 12, 0.5, 0.04, 'goldenrod', 'dodgerBlue4')
                image = PhotoImage(file = 'assets/images/axi.png')
                page = Label(scene4, image = image)
                page.place(relx = 0.5, rely = 0.53, anchor = CENTER)
                scene4.mainloop()


if __name__ == '__main__':
    main()