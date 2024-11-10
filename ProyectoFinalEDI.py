# Proyecto final de Estructura de Datos I
# Realizado por Paula Gómez, Ronald Arrieta, Antonella Giamaria y Camilo Acevedo

import cv2 # Se importa la librería OpenCV para el manejo y la gestión de archivos de videos

class Escena:
    """Clase que representa una escena del juego"""
    def __init__(self, escena, indice):
        self.escena = escena
        self.indice = indice

class Escenas:
    """Clase que representa una lista de escenas"""
    def __init__(self):
        self.head = None

    def add_escena(self, escena, indice):
        if self.head is None:
            self.head = Escena(escena, indice)
        else:
            current = self.head
            while current.escena is not None:
                current = current.escena
            current.escena = Escena(escena, indice)

    def show_escena(self, indice):
        current_escena = self.head
        while current_escena is not None:
            if current_escena.indice == indice:
                while current_escena.isOpened():
                    ret, frame = current_escena.read()
                    if not ret:
                        break
                    cv2.imshow('', frame)
                    if cv2.waitKey(15) == 27:
                        break
            current = current.escena

def main():
    escenas = Escenas()
    for i in range(1, 2): # Se cargan las escenas en la lista de escenas
        escena = cv2.VideoCapture(f'escena{i}.mp4')
        escenas.add_escena(escena, i)


    escenas.show_escena(1)

if __name__ == '__main__':
    main()