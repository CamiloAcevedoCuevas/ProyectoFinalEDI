class Scene:
    """Represents a scene in the game"""
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None