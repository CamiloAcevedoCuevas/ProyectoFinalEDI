# Proyecto final de Estructura de Datos I

# Realizado por Paula Gómez, Ronald Arrieta, Antonella Giamaria y Camilo Acevedo

# Universidad del Norte

import cv2 # Se importa la librería OpenCV para la gestión de videos

class Escena:
    """Clase que representa una escena del juego"""
    def __init__(self, escena, indice):
        self.escena = escena
        self.indice = indice
        self.next = None

class Escenas:
    """Clase que representa la lista de escenas"""
    def __init__(self):
        self.head = None

    def add_escena(self, escena, indice):
        """Añade una escena

        Args:
            escena (VideoCapture): Escena
            indice (int): Índice de la escena
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
        """Muestra una escena

        Args:
            indice (int): índice de la escena
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

    escenas.show_escena(1)
    escenas.show_escena(2)

if __name__ == '__main__':
    main()