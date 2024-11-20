class Scene:
    """Represents a scene in the game.
    
    Args:
        scene (cv2.VideoCapture): The video of the scene
        index (int): The index of the scene
    
    """
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None
        