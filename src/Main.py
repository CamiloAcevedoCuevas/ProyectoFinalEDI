# El Poder De Un Click
# By Nebula Games®

import cv2
import winsound
from tkinter import *
from GUI import GUI
from Scenes import Scenes
from Scores import Scores
    
def main():
    gui = GUI()
    scenes = Scenes()
    scores = Scores()
    
    for i in range(1, 6): # scenes buffering
        scene = cv2.VideoCapture(f'assets/videos/scene{i}.mp4')
        scenes.add_scene(scene, i)

    menu = Tk() # main menu
    gui.window = menu
    gui.set_window()
    bg = PhotoImage(file = 'assets/images/background.png')
    gui.set_img(bg, 0.5)
    logo = PhotoImage(file = 'assets/images/logo.png')
    gui.set_img(logo, 0.32)
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.set_btn('Iniciar Partida', start, 0.5, 0.6)
    gui.set_btn('Salir', exit, 0.5, 0.7)
    menu.mainloop()

    if scenes.scene == 'start':
        while True:
            scorage = 0
            start = Tk()
            gui.window = start
            gui.set_window()
            bg = PhotoImage(file = 'assets/images/background.png')
            gui.set_img(bg, 0.5)
            jvr = PhotoImage(file = 'assets/images/javier.png') # Javier's image
            gui.set_img(jvr, 0.4)
            gui.set_lbl(scenes.txt[0], 13, 0.88)
            winsound.PlaySound('assets/audios/javier.wav', winsound.SND_ASYNC) # Reproduce el audio donde se presenta a Javier.
            def scene1():
                scenes.scene = 1
                start.destroy()
            start.after(34000, scene1)
            start.mainloop()

            if scenes.scene == 1:
                scenes.get_scene(1, 5) # Reproduce la escena donde Javier se conecta al wifi.
                scene1 = Tk()
                gui.window = scene1
                gui.set_window()
                bg = PhotoImage(file = 'assets/images/background.png')
                gui.set_img(bg, 0.5)
                gui.set_lbl('¿Usted haría lo mismo que Javier?', 24, 0.2)
                def scene2():
                    scores.add_score(-5000)
                    scenes.scene = 2
                    scene1.destroy()
                def cograts():
                    scores.add_score(10000)
                    scenes.scene = 'congrats'
                    scene1.destroy()
                gui.set_btn(scenes.txt[1], scene2, 0.5, 0.5)
                gui.set_btn('No, es muy sospechoso', cograts, 0.5, 0.65)
                scene1.mainloop()   

                if scenes.scene == 2:
                    while True:
                        if scenes.scene == 2:
                            scenes.scene = None
                            scenes.get_scene(2, 9) # Muestra la secuencia donde Javier recuerda la conversación con su primo Juan.
                            scene2 = Tk()
                            gui.window = scene2
                            gui.set_window()
                            bg = PhotoImage(file = 'assets/images/background.png')
                            gui.set_img(bg, 0.5)
                            gui.set_lbl('¿Está seguro de que fue lo correcto?', 22, 0.2)
                            def reset():
                                scores.add_score(-5000)
                                scenes.scene = 2
                                scene2.destroy()
                            def next():
                                scores.add_score(10000)
                                scenes.scene = 'congrats'
                                scene2.destroy()
                            gui.set_btn(scenes.txt[1], reset, 0.5, 0.5)
                            gui.set_btn('No, es muy sospechoso', next, 0.5, 0.65)
                            scene2.mainloop()
                        else:
                            break  

                if scenes.scene == 'congrats':
                    winsound.PlaySound('assets/audios/congrats.wav', 0) # Reproduce el audio donde se felicita al jugador por haber identificado la actividad sospechosa.
                    window = Tk()
                    gui.window = window
                    gui.set_window()
                    bg = PhotoImage(file = 'assets/images/background.png')
                    gui.set_img(bg, 0.5)
                    def cookies():
                        scores.add_score(5000)
                        gui.set_lbl(scenes.txt[2], 16, 0.72)
                        gui.set_btn('¿Cookies?', None, 0.5, 0.5)
                        winsound.PlaySound('assets/audios/cookies.wav', winsound.SND_ASYNC) # Reproduce el audio con la explicación de las cookies.
                        def scene3():
                            scenes.scene = 3
                            window.destroy()
                        window.after(11000, scene3)
                    gui.set_btn('¿Cookies?', cookies, 0.5, 0.5)
                    window.mainloop() 

                    if scenes.scene == 3:
                        scenes.get_scene(3, 11) # Muestra la escena donde Javier encuentra Axi.
                        winsound.PlaySound('assets/audios/identify.wav', winsound.SND_ASYNC) # Reproduce el audio donde se pide identificar.
                        scene3 = Tk()
                        gui.window = scene3
                        gui.set_window()
                        bg = PhotoImage(file = 'assets/images/background.png')
                        gui.set_img(bg, 0.5)
                        axi = PhotoImage(file = 'assets/images/axi.png')
                        gui.set_img(axi, 0.53)
                        gui.set_lbl('Hay algo extraño en esta página, identifíquelo:', 14, 0.04)
                        def next():
                            scores.add_score(12000)
                            def next():
                                scores.add_score(12000)
                                def next():
                                    scores.add_score(12000)
                                    scenes.scene = 'window'
                                    winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                    scene3.destroy()
                                winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                gui.set_btn('Logo\nmodificado', next, 0.158, 0.28)
                            winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                            gui.set_btn('Escudo modificado', next, 0.42, 0.27)
                        gui.set_btn('Sin Protocolo de transferencia seguro (https)', next, 0.3, 0.205)
                        scene3.mainloop() 

                        if scenes.scene == 'window':
                            while True:
                                if scenes.scene == 'window':
                                    scenes.scene = None
                                    window = Tk()
                                    gui.window = window
                                    gui.set_window()
                                    bg = PhotoImage(file = 'assets/images/background.png')
                                    gui.set_img(bg, 0.5)
                                    brwser = PhotoImage(file = 'assets/images/browser.png')
                                    gui.set_img(brwser, 0.4)
                                    gui.set_lbl('¿Invirtiría usted en esta página?', 15, 0.8)
                                    def reset():
                                        scores.add_score(-5000)
                                        scenes.scene = 'window'
                                        scenes.get_scene(3, 11)
                                        window.destroy()
                                    def bank():
                                        scores.add_score(10000)
                                        scenes.scene = 'bank'
                                        window.destroy()
                                    gui.set_btn('SÍ, es una página segura', reset, 0.35, 0.9)
                                    gui.set_btn('No, es muy sospechoso', bank, 0.65, 0.9)
                                    window.mainloop()
                                else:
                                    break   

                            if scenes.scene == 'bank':
                                winsound.PlaySound('assets/audios/stop.wav', winsound.SND_ASYNC) 
                                bank = Tk()
                                gui.window = bank
                                gui.set_window()
                                bg = PhotoImage(file = 'assets/images/background.png')
                                gui.set_img(bg, 0.5)
                                bnk = PhotoImage(file = 'assets/images/bank.png')
                                gui.set_img(bnk, 0.53)
                                gui.set_lbl('Mire aquí una página de un sitio web oficial de un banco:', 14, 0.04)
                                def scene4():
                                    scores.add_score(2000)
                                    scenes.scene = 4
                                    bank.destroy()
                                gui.set_btn('Continuar', scene4, 0.5, 0.9)
                                bank.mainloop()     

                                if scenes.scene == 4:
                                    winsound.PlaySound('assets/audios/transition.wav', 0) # Reproduce el audio donde se explica Javier no se dió cuenta que la página era falsa y decidió invertir.
                                    scenes.get_scene(4, 13) # Muestra la escena donde Javier recibe el correo del banco.
                                    scene4 = Tk()
                                    gui.window = scene4
                                    gui.set_window()
                                    bg = PhotoImage(file = 'assets/images/background.png')
                                    gui.set_img(bg, 0.5)
                                    gui.set_lbl('¿Invertiría usted en esta página?', 22, 0.2)
                                    def reset():
                                        scores.add_score(-20000)
                                        scenes.get_scene(4, 13)
                                        scenes.scene = 'window'
                                        scene4.destroy()
                                    def next():
                                        scores.add_score(4000)
                                        scenes.scene = 'next'
                                        scene4.destroy()
                                    gui.set_btn('Si, y acepto el bono de inversión', reset, 0.35, 0.5)
                                    gui.set_btn('No, es muy sospechoso', next, 0.65, 0.5)
                                    scene4.mainloop() 

                                    if scenes.scene == 'window':
                                        window = Tk()
                                        gui.window = window
                                        gui.set_window()
                                        bg = PhotoImage(file = 'assets/images/background.png')
                                        gui.set_img(bg, 0.5)
                                        gui.set_lbl(scenes.txt[3], 13, 0.31)
                                        gui.set_lbl('¿Reinvirtiría usted en esta página?', 19, 0.7)
                                        def reset():
                                            scores.add_score(-15000)
                                        def next():
                                            scenes.scene = 'next'
                                            window.destroy()
                                        gui.set_btn('Si, y acepto el bono de inversión', reset, 0.35, 0.9)
                                        gui.set_btn('No, es muy sospechoso', next, 0.65, 0.9)
                                        window.mainloop()

                                    if scenes.scene == 'next':
                                        winsound.PlaySound('assets/audios/stop.wav', winsound.SND_ASYNC)
                                        window = Tk()
                                        gui.window = window
                                        gui.set_window()
                                        bg = PhotoImage(file = 'assets/images/background.png')
                                        gui.set_img(bg, 0.5)
                                        gui.set_lbl(scenes.txt[4], 16, 0.5)
                                        def scene5():
                                            scenes.scene = 5
                                            window.destroy()
                                        gui.set_btn('Continuar', scene5, 0.5, 0.9)
                                        window.mainloop() 

                                        if scenes.scene == 5:
                                            scenes.get_scene(5, 10) # Muestra la escena donde Javier está sin dinero, desesperado y sin trabajo.
                                            window = Tk()
                                            gui.window = window
                                            gui.set_window()
                                            bg = PhotoImage(file = 'assets/images/background.png')
                                            gui.set_img(bg, 0.5)
                                            gui.set_lbl(scenes.txt[5], 22, 0.2)
                                            def op1():
                                                scores.add_score(-5000)
                                                scenes.scene = 'op1'
                                                window.destroy()
                                            def op2():
                                                scores.add_score(50000)
                                                scenes.scene = 'op2'
                                                window.destroy()
                                            gui.set_btn('Hacer clic en el enlace y registrarse', op1, 0.5, 0.6)
                                            gui.set_btn('Ignorar el correo y no hacer clic', op2, 0.5, 0.8)
                                            window.mainloop()  

                                            if scenes.scene != 5:
                                                window = Tk()
                                                gui.window = window
                                                gui.set_window()
                                                bg = PhotoImage(file = 'assets/images/background.png')
                                                gui.set_img(bg, 0.5)
                                                if scenes.scene == 'op1':
                                                    # ws = PhotoImage(file = 'assets/images/website.png')
                                                    # gui.set_img(ws, 0.4)
                                                    gui.set_lbl('¿ingresaría usted sus datos?', 22, 0.2)
                                                    def txt():
                                                        gui.set_lbl(scenes.txt[6], 13, 0.75)
                                                    def end():
                                                        gui.set_lbl('¿Desea jugar de nuevo?', 26, 0.75)
                                                        gui.set_lbl(scenes.txt[7], 18, 0.3)
                                                        def reset():
                                                            window.destroy()
                                                        def exit():
                                                            scenes.scene = 'exit'
                                                            window.destroy()
                                                        gui.set_btn('Si', reset, 0.3, 0.9)    
                                                        gui.set_btn('No', exit, 0.7, 0.9)
                                                    gui.set_btn('Si', txt, 0.3, 0.9)
                                                    gui.set_btn('No', end, 0.7, 0.9)
                                                else:
                                                    gui.set_lbl('¿Desea jugar de nuevo?', 26, 0.75)
                                                    gui.set_lbl(scenes.txt[8], 18, 0.3)
                                                    def reset():
                                                        window.destroy()
                                                    def exit():
                                                        scenes.scene = 'exit'
                                                        window.destroy()
                                                    gui.set_btn('Si', reset, 0.35, 0.9)    
                                                    gui.set_btn('No', exit, 0.65, 0.9)
                                                window.mainloop()

                                            if scenes.scene == 5 or scenes.scene == 'exit':
                                                scorage = scores.get_scorage()
                                                print(scorage)
                                                break
                                        else:
                                            break
                                    else:
                                        break
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break

if __name__ == '__main__':
    main()
    