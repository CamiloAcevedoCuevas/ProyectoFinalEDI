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
    
class GUI ():
    """Graphical User Interface"""
    def __init__(self):
        self.window = Tk()

    def get_window(self):
        self.window.iconbitmap('Assets/logo/icon.ico')
        self.window.title('El Poder De Un Click')
        self.window.configure(background = 'white')
        self.window.geometry('1024x576')
        self.window.resizable(False, False)

    def get_label(self, text, x, y, size):
        label = Label(self.window, text = text, fg = 'black', bg = 'white', font = ('Arial', size))
        label.place(x = x, y = y)

    def get_button(self, text, x, y, width, height, command):
        button = Button(self.window, text = text, fg = 'black', bg = 'white', font = ('Arial', 12), command = command)
        button.place(x = x, y = y, width = width, height = height)

def main():
    scenes = Scenes()

    for i in range(1, 3): # Scenes Buffering
        scene = cv2.VideoCapture(f'Assets/scenes/scene{i}.mp4')
        scenes.add_scene(scene, i)

    gui = GUI()

    gui.get_window()
    gui.get_label('El Poder De Un Click', 370, 100, 24)
    
    def start ():
        gui.window.destroy()
        winsound.PlaySound('Assets/audios/aud1.wav', 0)
        scenes.get_scene(1)

    gui.get_button('Start', 450, 200, 120, 40, start)

    gui.window.mainloop()

if __name__ == '__main__':
    main()