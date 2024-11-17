class Image:
    """Class that represents an image."""
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.next = None
        self.prev = None