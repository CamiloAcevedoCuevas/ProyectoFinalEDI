class Scene:
    """Represents A Game Scene

    Args:
        scene (VideoCapture): Scene
        index (int): Scene Number
    """
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None