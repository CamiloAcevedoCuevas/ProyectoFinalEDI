from Image import Image

class Images:
    """List to store images."""
    def __init__(self):
        self.head = None

    def add_image(self, image):
        """Add An Image

        Args:
            image (PhotoImage): Image
        """
        if self.head is None:
            new_image = Image(image)
            self.head = new_image
            return
        current = self.head
        while current.next is not None:
            current = current.next
        new_image = Image(image)
        current.next = new_image
        new_image.prev = current

    def get_image(self, name):
        """Get An Image

        Args:
            name (str): Image Name
        """
        current = self.head
        while current is not None:
            if current.name == name:
                return current.image
            current = current.next
        return None