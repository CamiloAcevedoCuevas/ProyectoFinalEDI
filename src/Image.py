class Image:
    """Class that represents an image."""
    def __init__(self, image):
        self.image = image
        self.next = None
        self.prev = None