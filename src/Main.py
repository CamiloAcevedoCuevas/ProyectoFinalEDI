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
    
    for i in range(1, 7): # scenes buffering
        scene = cv2.VideoCapture(f'assets/videos/video{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk() # main menu
    gui.window = menu
    gui.set_window()
    img = PhotoImage(file = 'assets/images/background.png')
    background = Label(menu, image = img)
    background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    gui.set_lbl('El Poder De Un Click', 24, 0.5, 0.15, 'goldenrod', 'gray2')
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.set_btn('Iniciar Partida', start, 0.4, 0.8, 150, 40, 'goldenrod', 'gray10')
    gui.set_btn('Salir', exit, 0.6, 0.8, 150, 40, 'goldenrod', 'gray10')
    menu.mainloop()

    if scenes.scene == 'start':
        start = Tk()
        gui.window = start
        gui.set_window()
        img = PhotoImage(file = 'assets/images/background.png')
        background = Label(start, image = img)
        background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        gui.set_lbl('Él es Javier. Javier es un excéntrico empresario de bienes raíces.\nLleva una vida de ensueño en la ciudad de Nueva York y cuenta con innumerables inversiones exitosas.\nPero un día, todo eso cambió... Javier tiene un defecto, no sabe mucho sobre la seguridad en internet.\nTu deberás identificar si las acciones de Javier fueron las mejores o si aún tiene cosas que aprender.', 12, 0.5, 0.85, 'goldenrod', 'gray2')
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
            gui.set_window()
            img = PhotoImage(file = 'assets/images/background.png')
            background = Label(scene1, image = img)
            background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            gui.set_lbl('¿Usted haría lo mismo que Javier?', 22, 0.5, 0.2, 'goldenrod', 'gray2')
            def scene2():
                scenes.scene = 2
                scene1.destroy()
            def scene3():
                scenes.scene = 3
                scene1.destroy()
            gui.set_btn('SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo', scene2, 0.5, 0.5, 930, 40, 'goldenrod', 'gray10')
            gui.set_btn('No, es muy sospechoso', scene3, 0.5, 0.65, 250, 40, 'goldenrod', 'gray10')
            scene1.mainloop()

            if scenes.scene == 2:
                while True:
                    if scenes.scene == 2:
                        scenes.scene = None
                        scenes.play_scene(2) # Muestra la secuencia donde Javier recuerda la conversación con su primo Juan.
                        scene2 = Tk()
                        gui.window = scene2
                        gui.set_window()
                        img = PhotoImage(file = 'assets/images/background.png')
                        background = Label(scene2, image = img)
                        background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                        gui.set_lbl('¿Está seguro de que fue lo correcto?', 22, 0.5, 0.2, 'goldenrod', 'gray2')
                        def reset():
                            scenes.scene = 2
                            scene2.destroy()
                        def scene3():
                            scenes.scene = 3
                            scene2.destroy()
                        gui.set_btn('SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo', reset, 0.5, 0.5, 930, 40, 'goldenrod', 'gray10')
                        gui.set_btn('No, es muy sospechoso', scene3, 0.5, 0.65, 250, 40, 'goldenrod', 'gray10')
                        scene2.mainloop()
                    else:
                        break

            if scenes.scene == 3:
                scenes.play_scene(3) # Muestra la secuencia donde se felicita al jugador por haber identificado la actividad sospechosa.
                winsound.PlaySound('assets/audios/transicion.wav', 0) # Reproduce el audio donde explica que las cookies de Javier fueron robadas.
                scene3 = Tk()
                gui.window = scene3
                gui.set_window()
                img = PhotoImage(file = 'assets/images/background.png')
                background = Label(scene3, image = img)
                background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                def cookies():
                    gui.set_lbl('Las cookies son pequeños archivos de texto que los sitios web guardan en tu dispositivo cuando los visitas.\n Sirven para almacenar información sobre tu actividad en línea', 12, 0.5, 0.72, 'goldenrod', 'gray2')
                    winsound.PlaySound('assets/audios/cookies.wav', winsound.SND_ASYNC) # Reproduce el audio con la explicación de las cookies.
                    scenes.scene = 4
                    scene3.after(5000, scene3.destroy)
                gui.set_btn('¿Cookies?', cookies, 0.5, 0.5, 150, 40, 'goldenrod', 'gray10')
                scene3.mainloop()
                
                if scenes.scene == 4:
                    while True:
                        if scenes.scene == 4:
                            scenes.scene = None
                            scenes.play_scene(4) # Muestra la escena donde Javier encuentra Axi.
                            scene4 = Tk()
                            gui.window = scene4
                            gui.set_window()
                            img = PhotoImage(file = 'assets/images/background.png')
                            background = Label(scene4, image = img)
                            background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                            im = PhotoImage(file = 'assets/images/axi.png')
                            page = Label(scene4, image = im)
                            page.place(relx = 0.5, rely = 0.53, anchor = CENTER)
                            gui.set_lbl('Hay algo extraño en esta página, identifíquelo:', 12, 0.5, 0.04, 'goldenrod', 'gray2')
                            def next():
                                def next():
                                    def next():
                                        scenes.scene = 'window'
                                        winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                        scene4.destroy()
                                    winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                    gui.set_btn('Logo\nmodificado', next, 0.13, 0.26, 98, 38, 'black', 'brown1')
                                winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                gui.set_btn('Escudo modificado', next, 0.4, 0.3, 160, 19, 'black', 'brown1')
                            gui.set_btn('Sin Protocolo de transferencia seguro (https)', next, 0.28, 0.17, 380, 19, 'black', 'brown1')
                            scene4.mainloop()

                        if scenes.scene == 'window':
                            scenes.scene = None
                            window = Tk()
                            gui.window = window
                            gui.set_window()
                            img = PhotoImage(file = 'assets/images/background.png')
                            background = Label(window, image = img)
                            background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                            gui.set_lbl('¿Invirtiría usted en esta página?', 22, 0.5, 0.2, 'goldenrod', 'gray2')
                            def reset():
                                scenes.scene = 4
                                window.destroy()
                            def bank():
                                scenes.scene = 'bank'
                                window.destroy()
                            gui.set_btn('SÍ, es una página segura', reset, 0.35, 0.5, 260, 40, 'goldenrod', 'gray10')
                            gui.set_btn('No, es muy sospechoso', bank, 0.65, 0.5, 250, 40, 'goldenrod', 'gray10')
                            window.mainloop()
                        else:
                            break

                    if scenes.scene == 'bank':
                        bank = Tk()
                        gui.window = bank
                        gui.set_window()
                        img = PhotoImage(file = 'assets/images/background.png')
                        background = Label(bank, image = img)
                        background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                        im = PhotoImage(file = 'assets/images/bank.png')
                        page = Label(bank, image = im)
                        page.place(relx = 0.5, rely = 0.53, anchor = CENTER)
                        gui.set_lbl('Mire aquí una página de un sitio web oficial de un banco:', 12, 0.5, 0.04, 'goldenrod', 'gray2')
                        bank.after(5000, bank.destroy)
                        bank.mainloop()
                        
                        winsound.PlaySound('assets/audios/transition.wav', 0) # Reproduce el audio donde se explica Javier no se dió cuenta que la página era falsa y decidió invertir.
     
                        scenes.play_scene(5) # Muestra la escena donde Javier recibe el correo del banco.
                        scene5 = Tk()
                        gui.window = scene5
                        gui.set_window()
                        img = PhotoImage(file = 'assets/images/background.png')
                        background = Label(scene5, image = img)
                        background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                        gui.set_lbl('¿Invertiría usted en esta página?', 22, 0.5, 0.2, 'goldenrod', 'gray2')
                        def reset():
                            scenes.play_scene(5)
                            scenes.scene = 'window'
                            scene5.destroy()
                        def next():
                            scenes.scene = 'next'
                            scene5.destroy()
                        gui.set_btn('Si, y acepto el bono de inversión', reset, 0.35, 0.5, 290, 40, 'goldenrod', 'gray10')
                        gui.set_btn('No, es muy sospechoso', next, 0.65, 0.5, 230, 40, 'goldenrod', 'gray10')
                        scene5.mainloop()

                        while True:
                            if scenes.scene == 'window':
                                scenes.scene = None
                                window = Tk()
                                gui.window = window
                                gui.set_window()
                                img = PhotoImage(file = 'assets/images/background.png')
                                background = Label(window, image = img)
                                background.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                                gui.set_lbl('¡Ups! Parece que has tomado una mala decisión.\nEl enlace que acabas de hacer clic no era un bono legítimo, sino una trampa diseñada\npara robar tus datos. Las estafas en línea pueden ser muy\nengañosas, y este tipo de fraude es más común de lo que parece.\n\n¿Por qué es una estafa?\n\n-Los enlaces que prometen bonos irresistibles suelen ser intentos de robar tu\ninformación personal o financiera.\n\n-Las empresas legítimas nunca pedirán tus datos por medio de enlaces\no correos sospechosos.', 12, 0.5, 0.25, 'goldenrod', 'gray2')
                                gui.set_lbl('¿Reinvirtiría usted en esta página?', 22, 0.5, 0.7, 'goldenrod', 'gray2')
                                def reset():
                                    scenes.scene = 'window'
                                    scenes.play_scene(5)
                                    window.destroy()
                                def next():
                                    scenes.scene = 'next'
                                    window.destroy()
                                gui.set_btn('Si, y acepto el bono de inversión', reset, 0.35, 0.9, 270, 40, 'goldenrod', 'gray10')
                                gui.set_btn('No, es muy sospechoso', next, 0.65, 0.9, 250, 40, 'goldenrod', 'gray10')
                                window.mainloop()
                            else:
                                break

                        if scenes.scene == 'next':
                            pass

if __name__ == '__main__':
    main()