from Scene import Scene
import cv2
import winsound

class Scenes:
    """Game Scenes"""
    def __init__(self):
        self.head = None

    def add_scene(self, scene, index):
        """Add An Scene

        Args:
            scene (VideoCapture): 
            index (int): Scene Number
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
        """Play An Scene

        Args:
            index (int): Scene number
        """
        winsound.PlaySound(f'Assets/Audios/Audio{index}', winsound.SND_ASYNC)
        current = self.head
        while current is not None:
            if current.index == index:
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('', frame)
                        cv2.waitKey(15)
                    else:
                        break
                break
            current = current.next