class Scene:
    """Represents A Game Scene"""
    def __init__(self, scene, index):
        self.scene = scene
        self.index = index
        self.next = None