# El Poder De Un Click
# Desarrollado por: Nebula Games ®

import cv2 # Video Management
from tkinter import * # GUI
import winsound # Audio Management

class Escena:
    """Escena del juego"""
    def __init__(self, escena, indice):
        self.escena = escena
        self.indice = indice
        self.next = None

class Escenas:
    """Lista de escenas"""
    def __init__(self):
        self.head = None

    def add_escena(self, escena, indice):
        """Añadir escena

        Args:
            escena (VideoCapture): 
            indice (int): 
        """
        new_escena = Escena(escena, indice)
        if self.head is None:
            self.head = new_escena
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_escena

    def get_escena(self, indice):
        """Mostrar escena

        Args:
            indice (int): 
        """
        current = self.head
        while current is not None:
            if current.indice == indice:
                while True:
                    ret, frame = current.escena.read()
                    if ret:
                        cv2.imshow('', frame)
                        if cv2.waitKey(15) == 27:
                            break
                    else:
                        break
                break
            current = current.next

def main():
    escenas = Escenas()

    for i in range(1, 3): # Buffering de escenas en memoria
        escena = cv2.VideoCapture(f'escena{i}.mp4')
        escenas.add_escena(escena, i)

    window = Tk()

    # window.iconbitmap('icon.ico')
    window.title('El Poder De Un Click')
    window.configure(background = 'gray')
    window.geometry('1024x576')
    window.resizable(False, False)

    startLabel = Label(window, text = 'El Poder De Un Click', fg = 'black', bg = 'gray', font = ('Arial', 24))
    startLabel.place(x = 370, y = 100)
    def start():
        window.destroy()
        winsound.PlaySound('audio1.wav', 0)
        escenas.get_escena(1)
    
    btnStart = Button(window, text = 'Start', fg = 'black', bg = 'white', font = ('Arial', 12), command = start)
    btnStart.place(x = 470, y = 200, width = 100, height = 30)

    window.mainloop()

if __name__ == '__main__':
    main()