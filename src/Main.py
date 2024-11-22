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
    
    for i in range(1, 8): # scenes buffering
        scene = cv2.VideoCapture(f'assets/videos/scene{i}.mp4')
        scenes.addScene(scene, i)

    menu = Tk() # main menu
    gui.window = menu
    gui.setWindow()
    bg = PhotoImage(file = 'assets/images/background.png')
    gui.setImg(bg, 0.5)
    logo = PhotoImage(file = 'assets/images/logo.png')
    gui.setImg(logo, 0.32)
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.setBtn('Iniciar Partida', start, 0.5, 0.6)
    gui.setBtn('Salir', exit, 0.5, 0.7)
    menu.mainloop()

    if scenes.scene == 'start':
        start = Tk()
        gui.window = start
        gui.setWindow()
        bg = PhotoImage(file = 'assets/images/background.png')
        gui.setImg(bg, 0.5)
        jvr = PhotoImage(file = 'assets/images/javier.png') # Javier's image
        gui.setImg(jvr, 0.4)
        gui.setLbl(scenes.txt[0], 13, 0.88)
        winsound.PlaySound('assets/audios/javier.wav', winsound.SND_ASYNC) # Reproduce el audio donde se presenta a Javier.
        def scene1():
            scenes.scene = 1
            start.destroy()
        start.after(34000, scene1)
        start.mainloop()

        if scenes.scene == 1:
            scenes.getScene(1, 5) # Reproduce la escena donde Javier se conecta al wifi.
            scene1 = Tk()
            gui.window = scene1
            gui.setWindow()
            bg = PhotoImage(file = 'assets/images/background.png')
            gui.setImg(bg, 0.5)
            gui.setLbl('¿Usted haría lo mismo que Javier?', 22, 0.2)
            def scene2():
                scenes.scene = 2
                scene1.destroy()
            def scene3():
                scenes.scene = 3
                scene1.destroy()
            gui.setBtn(scenes.txt[1], scene2, 0.5, 0.5)
            gui.setBtn('No, es muy sospechoso', scene3, 0.5, 0.65)
            scene1.mainloop()

            if scenes.scene == 2:
                while True:
                    if scenes.scene == 2:
                        scenes.scene = None
                        scenes.getScene(2, 9) # Muestra la secuencia donde Javier recuerda la conversación con su primo Juan.
                        scene2 = Tk()
                        gui.window = scene2
                        gui.setWindow()
                        bg = PhotoImage(file = 'assets/images/background.png')
                        gui.setImg(bg, 0.5)
                        gui.setLbl('¿Está seguro de que fue lo correcto?', 22, 0.2)
                        def reset():
                            scenes.scene = 2
                            scene2.destroy()
                        def scene3():
                            scenes.scene = 3
                            scene2.destroy()
                        gui.setBtn(scenes.txt[1], reset, 0.5, 0.5)
                        gui.setBtn('No, es muy sospechoso', scene3, 0.5, 0.65)
                        scene2.mainloop()
                    else:
                        break

            if scenes.scene == 3:
                scenes.getScene(3, 0) # Muestra la secuencia donde se felicita al jugador por haber identificado la actividad sospechosa.
                winsound.PlaySound('assets/audios/transition1.wav', 0) # Reproduce el audio donde explica que las cookies de Javier fueron robadas.
                scene3 = Tk()
                gui.window = scene3
                gui.setWindow()
                bg = PhotoImage(file = 'assets/images/background.png')
                gui.setImg(bg, 0.5)
                def cookies():
                    gui.setLbl(scenes.txt[2], 13, 0.72)
                    winsound.PlaySound('assets/audios/cookies.wav', winsound.SND_ASYNC) # Reproduce el audio con la explicación de las cookies.
                    def scene4():
                        scenes.scene = 4
                        scene3.destroy()
                    scene3.after(10000, scene4)
                gui.setBtn('¿Cookies?', cookies, 0.5, 0.5)
                scene3.mainloop()

                if scenes.scene == 4:
                    scenes.getScene(4, 0) # Muestra la escena donde Javier encuentra Axi.
                    scene4 = Tk()
                    gui.window = scene4
                    gui.setWindow()
                    bg = PhotoImage(file = 'assets/images/background.png')
                    gui.setImg(bg, 0.5)
                    axi = PhotoImage(file = 'assets/images/axi.png')
                    gui.setImg(axi, 0.53)
                    gui.setLbl('Hay algo extraño en esta página, identifíquelo:', 14, 0.04)
                    def next():
                        def next():
                            def next():
                                scenes.scene = 'window'
                                winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                scene4.destroy()
                            winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                            gui.setBtn('Logo\nmodificado', next, 0.158, 0.28)
                        winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                        gui.setBtn('Escudo modificado', next, 0.42, 0.27)
                    gui.setBtn('Sin Protocolo de transferencia seguro (https)', next, 0.3, 0.205)
                    scene4.mainloop()

                    if scenes.scene == 'window':
                        while True:
                            if scenes.scene == 'window':
                                scenes.scene = None
                                window = Tk()
                                gui.window = window
                                gui.setWindow()
                                bg = PhotoImage(file = 'assets/images/background.png')
                                gui.setImg(bg, 0.5)
                                brwser = PhotoImage(file = 'assets/images/browser.png')
                                gui.setImg(brwser, 0.4)
                                gui.setLbl('¿Invirtiría usted en esta página?', 15, 0.8)
                                def reset():
                                    scenes.scene = 'window'
                                    scenes.getScene(4, 0)
                                    window.destroy()
                                def bank():
                                    scenes.scene = 'bank'
                                    window.destroy()
                                gui.setBtn('SÍ, es una página segura', reset, 0.35, 0.9)
                                gui.setBtn('No, es muy sospechoso', bank, 0.65, 0.9)
                                window.mainloop()
                            else:
                                break

                        if scenes.scene == 'bank':
                            bank = Tk()
                            gui.window = bank
                            gui.setWindow()
                            bg = PhotoImage(file = 'assets/images/background.png')
                            gui.setImg(bg, 0.5)
                            bnk = PhotoImage(file = 'assets/images/bank.png')
                            gui.setImg(bnk, 0.53)
                            gui.setLbl('Mire aquí una página de un sitio web oficial de un banco:', 14, 0.04)
                            def scene5():
                                scenes.scene = 5
                                bank.destroy()
                            bank.after(5000, scene5)
                            bank.mainloop()

                            if scenes.scene == 5:
                                winsound.PlaySound('assets/audios/transition2.wav', 0) # Reproduce el audio donde se explica Javier no se dió cuenta que la página era falsa y decidió invertir.
                                scenes.getScene(5, 0) # Muestra la escena donde Javier recibe el correo del banco.
                                scene5 = Tk()
                                gui.window = scene5
                                gui.setWindow()
                                bg = PhotoImage(file = 'assets/images/background.png')
                                gui.setImg(bg, 0.5)
                                gui.setLbl('¿Invertiría usted en esta página?', 22, 0.2)
                                def reset():
                                    scenes.getScene(5, 0)
                                    scenes.scene = 'window'
                                    scene5.destroy()
                                def next():
                                    scenes.scene = 'next'
                                    scene5.destroy()
                                gui.setBtn('Si, y acepto el bono de inversión', reset, 0.35, 0.5)
                                gui.setBtn('No, es muy sospechoso', next, 0.65, 0.5)
                                scene5.mainloop()

                                while True:
                                    if scenes.scene == 'window':
                                        scenes.scene = None
                                        window = Tk()
                                        gui.window = window
                                        gui.setWindow()
                                        bg = PhotoImage(file = 'assets/images/background.png')
                                        gui.setImg(bg, 0.5)
                                        gui.setLbl(scenes.txt[3], 13, 0.31)
                                        gui.setLbl('¿Reinvirtiría usted en esta página?', 19, 0.7)
                                        def reset():
                                            scenes.scene = 'window'
                                            window.destroy()
                                        def next():
                                            scenes.scene = 'next'
                                            window.destroy()
                                        gui.setBtn('Si, y acepto el bono de inversión', reset, 0.35, 0.9)
                                        gui.setBtn('No, es muy sospechoso', next, 0.65, 0.9)
                                        window.mainloop()
                                    else:
                                        break

                                if scenes.scene == 'next':
                                    window = Tk()
                                    gui.window = window
                                    gui.setWindow()
                                    bg = PhotoImage(file = 'assets/images/background.png')
                                    gui.setImg(bg, 0.5)
                                    gui.setLbl(scenes.txt[4], 12, 0.5)
                                    window.mainloop()
                                    scenes.getScene(6, 0) # Muestra la escena donde Javier está sin dinero, desesperado y sin trabajo.

if __name__ == '__main__':
    main()
    