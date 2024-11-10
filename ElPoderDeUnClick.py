# Desarrollado por Nebula Games ©

import cv2 # Manejo de video
from tkinter import * # Interfaz gráfica

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
            escena (VideoCapture): _description_
            indice (int): _description_
        """
        new_escena = Escena(escena, indice)
        if self.head is None:
            self.head = new_escena
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_escena

    def show_escena(self, indice):
        """Mostrar escena

        Args:
            indice (int): _description_
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

    # escenas.show_escena(1)
    # escenas.show_escena(2)

    window = Tk()

    # window.iconbitmap('icon.ico')
    window.title('El Poder De Un Click')
    window.geometry('1024x576')
    window.resizable(False, False)

    startLabel = Label(window, text = 'El Poder De Un Click', font = ('Arial', 24))
    startLabel.place(x = 370, y = 100)

    def start():
        window.destroy()
        escenas.show_escena(1)

    btnStart = Button(window, text = 'Start', command = start)
    btnStart.place(x = 512, y = 288)
    btnStart.pack()

    window.mainloop()

if __name__ == '__main__':
    main()