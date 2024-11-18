from Scene import Scene
import cv2
import winsound

class Scenes:
    """List Of Scenes"""
    def __init__(self):
        self.scene = None
        self.head = None

    def addScene(self, scene, index):
        """Add A Scene

        Args:
            scene (cv2.VideoCapture): Scene Video
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

    def getScene(self, index):
        """Play A Scene

        Args:
            index (int): Scene Number
        """
        current = self.head
        while current is not None:
            if current.index == index:
                winsound.PlaySound(f'assets/audios/audio{index}.wav', winsound.SND_ASYNC) # Here the audio of the scene is played.
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('El Poder De Un Click', frame)
                        cv2.waitKey(20)
                    else:
                        break
                cv2.destroyAllWindows()
                break
            current = current.next