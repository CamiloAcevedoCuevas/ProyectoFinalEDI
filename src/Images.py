from Image import Image

class Images:
    """Class to store images."""
    def __init__(self):
        self.image = None

    def add_image(self, image):
        if self.image is None:
            new_image = Image(image)