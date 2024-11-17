from Scene import Scene
import cv2
import winsound

class Scenes:
    """Class that stores the scenes of the game."""
    def __init__(self):
        self.scene = None
        self.head = None

    def add_scene(self, scene, index):
        """Function to add a scene to the list.

        Args:
            scene (VideoCapture): Scene Video
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

    def play_scene(self, index):
        """This function plays the scene video.

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