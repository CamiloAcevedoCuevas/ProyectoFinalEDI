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
        scenes.addScene(scene, i)

    bgPath = 'assets/images/background.png'
    txt = ['Él es Javier. Javier es un excéntrico empresario de bienes raíces.\nLleva una vida de ensueño en la ciudad de Nueva York y cuenta con innumerables inversiones exitosas.\nPero un día, todo eso cambió... Javier tiene un defecto, no sabe mucho sobre la seguridad en internet.\nTu deberás identificar si las acciones de Javier fueron las mejores o si aún tiene cosas que aprender.',
            'SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo',
            'Las cookies son pequeños archivos de texto que los sitios web guardan en tu dispositivo cuando los visitas.\n Sirven para almacenar información sobre tu actividad en línea',
            '¡Ups! Parece que has tomado una mala decisión.\n\nEl enlace que acabas de hacer clic no era un bono legítimo, sino una trampa diseñada\npara robar tus datos. Las estafas en línea pueden ser muy\nengañosas, y este tipo de fraude es más común de lo que parece.\n\n¿Por qué es una estafa?\n\n1. Los enlaces que prometen bonos irresistibles suelen ser intentos de robar tu\ninformación personal o financiera.\n\n2. Las empresas legítimas nunca pedirán tus datos por medio de enlaces\no correos sospechosos.',
            '¡Ahora sabes cómo identificar una estafa!\n\nPara avanzar en este juego, asegúrate de tomar decisiones más sabias y proteger tus recursos.\nSi haces clic en ofertas dudosas, podrías perder más que solo dinero.\n\n¡Ten cuidado y no dejes que te engañen, recuerda que lo mejor es DENUNCIAR!']
    

    menu = Tk() # main menu
    gui.window = menu
    gui.setWindow()
    bg = PhotoImage(file = bgPath)
    gui.setImg(bg, 0.5)
    gui.setLbl('El Poder De Un Click', 24, 0.15)
    def start():
        scenes.scene = 'start'
        menu.destroy()
    def exit():
        menu.destroy()
    gui.setBtn('Iniciar Partida', start, 0.4, 0.8)
    gui.setBtn('Salir', exit, 0.6, 0.8)
    menu.mainloop()

    if scenes.scene == 'start':
        start = Tk()
        gui.window = start
        gui.setWindow()
        bg = PhotoImage(file = bgPath)
        gui.setImg(bg, 0.5)
        # jvr = PhotoImage(file = 'assets/images/javier.png') # Javier's image
        # gui.setImg(jvr, 0.5, 0.3)
        gui.setLbl(txt[0], 12, 0.85)
        winsound.PlaySound('assets/audios/javier.wav', winsound.SND_ASYNC) # Reproduce el audio donde se presenta a Javier.
        def scene1():
            scenes.scene = 1
            start.destroy()
        start.after(5000, scene1)
        start.mainloop()

        if scenes.scene == 1:
            scenes.getScene(1) # Reproduce la escena donde Javier se conecta al wifi.
            scene1 = Tk()
            gui.window = scene1
            gui.setWindow()
            bg = PhotoImage(file = bgPath)
            gui.setImg(bg, 0.5)
            gui.setLbl('¿Usted haría lo mismo que Javier?', 22, 0.2)
            def scene2():
                scenes.scene = 2
                scene1.destroy()
            def scene3():
                scenes.scene = 3
                scene1.destroy()
            gui.setBtn(txt[1], scene2, 0.5, 0.5)
            gui.setBtn('No, es muy sospechoso', scene3, 0.5, 0.65)
            scene1.mainloop()

            if scenes.scene == 2:
                while True:
                    if scenes.scene == 2:
                        scenes.scene = None
                        scenes.getScene(2) # Muestra la secuencia donde Javier recuerda la conversación con su primo Juan.
                        scene2 = Tk()
                        gui.window = scene2
                        gui.setWindow()
                        bg = PhotoImage(file = bgPath)
                        gui.setImg(bg, 0.5)
                        gui.setLbl('¿Está seguro de que fue lo correcto?', 22, 0.2)
                        def reset():
                            scenes.scene = 2
                            scene2.destroy()
                        def scene3():
                            scenes.scene = 3
                            scene2.destroy()
                        gui.setBtn(txt[1], reset, 0.5, 0.5)
                        gui.setBtn('No, es muy sospechoso', scene3, 0.5, 0.65)
                        scene2.mainloop()
                    else:
                        break

            if scenes.scene == 3:
                scenes.getScene(3) # Muestra la secuencia donde se felicita al jugador por haber identificado la actividad sospechosa.
                winsound.PlaySound('assets/audios/transicion.wav', 0) # Reproduce el audio donde explica que las cookies de Javier fueron robadas.
                scene3 = Tk()
                gui.window = scene3
                gui.setWindow()
                bg = PhotoImage(file = bgPath)
                gui.setImg(bg, 0.5)
                def cookies():
                    gui.setLbl(txt[2], 12, 0.72)
                    winsound.PlaySound('assets/audios/cookies.wav', winsound.SND_ASYNC) # Reproduce el audio con la explicación de las cookies.
                    def scene4():
                        scenes.scene = 4
                        scene3.destroy()
                    scene3.after(5000, scene4)
                gui.setBtn('¿Cookies?', cookies, 0.5, 0.5)
                scene3.mainloop()
                
                if scenes.scene == 4:
                    scenes.getScene(4) # Muestra la escena donde Javier encuentra Axi.
                    scene4 = Tk()
                    gui.window = scene4
                    gui.setWindow()
                    bg = PhotoImage(file = bgPath)
                    gui.setImg(bg, 0.5)
                    axi = PhotoImage(file = 'assets/images/axi.png')
                    gui.setImg(axi, 0.53)
                    gui.setLbl('Hay algo extraño en esta página, identifíquelo:', 12, 0.04)
                    def next():
                        def next():
                            def next():
                                scenes.scene = 'window'
                                winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                                scene4.destroy()
                            winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                            gui.setBtn('Logo\nmodificado', next, 0.13, 0.26)
                        winsound.PlaySound('assets/audios/click.wav', winsound.SND_ASYNC)
                        gui.setBtn('Escudo modificado', next, 0.4, 0.3)
                    gui.setBtn('Sin Protocolo de transferencia seguro (https)', next, 0.28, 0.17)
                    scene4.mainloop()

                    if scenes.scene == 'window':
                        while True:
                            if scenes.scene == 'window':
                                scenes.scene = None
                                window = Tk()
                                gui.window = window
                                gui.setWindow()
                                bg = PhotoImage(file = bgPath)
                                gui.setImg(bg, 0.5)
                                brwser = PhotoImage(file = 'assets/images/browser.png')
                                gui.setImg(brwser, 0.4)
                                gui.setLbl('¿Invirtiría usted en esta página?', 15, 0.8)
                                def reset():
                                    scenes.scene = 'window'
                                    scenes.getScene(4)
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
                            bg = PhotoImage(file = bgPath)
                            gui.setImg(bg, 0.5)
                            bnk = PhotoImage(file = 'assets/images/bank.png')
                            gui.setImg(bnk, 0.53)
                            gui.setLbl('Mire aquí una página de un sitio web oficial de un banco:', 12, 0.04)
                            def scene5():
                                scenes.scene = 5
                                bank.destroy()
                            bank.after(5000, scene5)
                            bank.mainloop()

                            if scenes.scene == 5:
                                winsound.PlaySound('assets/audios/transition.wav', 0) # Reproduce el audio donde se explica Javier no se dió cuenta que la página era falsa y decidió invertir.
                                scenes.getScene(5) # Muestra la escena donde Javier recibe el correo del banco.
                                scene5 = Tk()
                                gui.window = scene5
                                gui.setWindow()
                                bg = PhotoImage(file = bgPath)
                                gui.setImg(bg, 0.5)
                                gui.setLbl('¿Invertiría usted en esta página?', 22, 0.2)
                                def reset():
                                    scenes.getScene(5)
                                    scenes.scene = 'window'
                                    scene5.destroy()
                                def next():
                                    scenes.scene = 'next'
                                    scene5.destroy()
                                gui.setBtn('Si, y acepto el bono de inversión', reset, 0.35, 0.5)
                                gui.setBtn('No, es muy sospechoso', next, 0.65, 0.5)
                                winsound.PlaySound('assets/audios/audio.wav', winsound.SND_ASYNC) # Reproduce el audio donde se pregunta se teniendo en cuenta lo ocurrido usted habría aceptado el bono.
                                scene5.mainloop()

                                while True:
                                    if scenes.scene == 'window':
                                        scenes.scene = None
                                        window = Tk()
                                        gui.window = window
                                        gui.setWindow()
                                        bg = PhotoImage(file = bgPath)
                                        gui.setImg(bg, 0.5)
                                        gui.setLbl(txt[3], 13, 0.31)
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
                                    bg = PhotoImage(file = bgPath)
                                    gui.setImg(bg, 0.5)
                                    gui.setLbl(txt[4], 12, 0.5)
                                    window.mainloop()
                                    scenes.getScene(6) # Muestra la escena donde Javier está sin dinero, desesperado y sin trabajo.

if __name__ == '__main__':
    main()