from image_manager import *

class Item:
    """The parent class for all items."""

    def __init__(self) -> None:

        self.name = "Item"
        self.image = None
        self.weight = int
        self.properties = None
        self.type = ""

    def set_name(self, new_name: str):
        """Set name of item."""
        self.name = new_name

    def get_name(self):
        return self.name

    def set_weight(self, new_weight: int):
        """Set weight of item."""
        self.weight = new_weight

    def get_weight(self):
        """Get the weight of the item."""
        return self.weight
    
    def set_type(self, new_type):
        """Set Item type."""
        self.type = new_type

    def get_type(self):
        """Get Item type."""
        return self.type

    def set_properties(self, properties):
        """Set properties of item. Whatever those are."""
        self.properties = properties

    def get_properties(self):
        """Get properties of item."""
        return self.properties

    def set_image(self, image_name: str):
        """Set the image of the item. Enter the name of an image from the list in image_manager.py"""
        self.image = Image(image_name)

    def get_image(self):
        """Get the image of the item."""
        return self.image




# Use this example item class as a reference when making items. Make sure to put them under Item class.
# Ignore the properties varible for now. Still trying to figure out.
class ExampleItem(Item):
    """Description"""

    def __init__(self) -> None:
        super().__init__()

        self.set_name("Example Name")
        self.set_weight(100)
        self.set_image("Trogdor")
        self.set_type("Quest")