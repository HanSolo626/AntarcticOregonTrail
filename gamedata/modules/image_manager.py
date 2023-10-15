# This is the image manager. To access images, you import image_manager
# and use 'Image("<image name>")' to get your image. If you want to add
# images, put in 'self.image_dict' with this format: ' "name":"image path" '.

import pygame

class ImageManager:
    def __init__(self) -> None:
        

        # Put image references here.
        self.image_dict = {
            
            # Test image.
            "Trogdor":"trogdor1_still.png",

            # Test background
            "Test Background":"test_bacground.png",

            "ArrowRight":"black_arrow_right.png"

        }


        # Do not change!
        self.image_path = "OregonTrail/gamedata/images/"


        # Prep images
        for image in self.image_dict:
            self.image_dict[image] = pygame.image.load(self.image_path+self.image_dict[image])


    def get_image(self, image_name: str):
        """Returns Surface Pygame object."""
        return self.image_dict[image_name]
    
    def get_image_dict(self):
        """Get the image dictionary."""
        return self.image_dict
    
class Image(ImageManager):
    def __init__(self, image_name: str) -> None:
        super().__init__()

        return self.get_image(image_name)
    
    