# El poder de un click

# Desarrollado por Nebula Games ©

import cv2
from tkinter import *

class Escena:
    def __init__(self, escena, indice):
        self.escena = escena
        self.indice = indice
        self.next = None

class Escenas:
    def __init__(self):
        self.head = None

    def add_escena(self, escena, indice):
        new_escena = Escena(escena, indice)
        if self.head is None:
            self.head = new_escena
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_escena

    def show_escena(self, indice):
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

    def close_escena(self):
        raiz = Tk()
        raiz.destroy()

def main():
    escenas = Escenas()

    for i in range(1, 3): # Buffering de escenas en memoria
        escena = cv2.VideoCapture(f'escena{i}.mp4')
        escenas.add_escena(escena, i)

    # escenas.show_escena(1)
    # escenas.show_escena(2)

    raiz = Tk()
    raiz.geometry('1024x576')
    raiz.title('Proyecto Final EDI')

    captureFrame = Frame()
    captureFrame.config(width = 1024, height = 576)
    captureFrame.place(x = 0, y = 0)

    btnFrame = Frame()
    btnFrame.config(width = 1024, height = 100)
    btnFrame.place(x = 0, y = 0)

    captureLabel = Label(captureFrame)
    captureLabel.place(x = 0, y = 0)

    btnCerrar = Button(btnFrame, text = 'Cerrar', command = print("XD"))
    #btnCerrar.place(x = 100, y = 40)
    btnCerrar.pack()

    raiz.mainloop()

if __name__ == '__main__':
    main()