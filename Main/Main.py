# El Poder De Un Click
# Desarrollado por: Nebula Games ®

import cv2 # Video Management
from tkinter import * # GUI
import winsound # Audio Management

class Scene:
    """Game Scene"""
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None

class Scenes:
    """Scenes"""
    def __init__(self):
        self.head = None

    def add_scene(self, scene, index):
        """Add scene

        Args:
            scene (VideoCapture): 
            index (int): 
        """
        new_scene = Scene(scene, index)
        if self.head is None:
            self.head = new_scene
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_scene

    def get_scene(self, index):
        """Play scene

        Args:
            index (int): 
        """
        current = self.head
        while current is not None:
            if current.index == index:
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('', frame)
                        if cv2.waitKey(15) == 27:
                            break
                    else:
                        break
                break
            current = current.next

def main():
    scenes = Scenes()

    for i in range(1, 3): # Scenes Buffering
        scene = cv2.VideoCapture(f'Assets/scenes/scene{i}.mp4')
        scenes.add_scene(scene, i)

    window = Tk()

    window.iconbitmap('Assets/logo/icon.ico')
    window.title('El Poder De Un Click')
    window.configure(background = 'gray')
    window.geometry('1024x576')
    window.resizable(False, False)

    startLabel = Label(window, text = 'El Poder De Un Click', fg = 'black', bg = 'gray', font = ('Arial', 24))
    startLabel.place(x = 370, y = 100)
    def start():
        window.destroy()
        winsound.PlaySound('Assets/audios/aud1.wav', 0)
        scenes.get_scene(1)
    
    btnStart = Button(window, text = 'Start', fg = 'black', bg = 'white', font = ('Arial', 12), command = start)
    btnStart.place(x = 470, y = 200, width = 100, height = 30)

    window.mainloop()

if __name__ == '__main__':
    main()