from gamedata.modules.save_manager import SaveManager

import sys

class VariableManager:
    """The class that manages the modification of important variables such as health of actors and points."""

    def __init__(self) -> None:
        
        # Load an instance of SaveManager
        self.save_manager = SaveManager()

        self.current_page = None




    def get_current_page(self):
        """Returns the current page object"""
        return self.current_page

    def get_current_save_data(self):
        """Returns current save object."""
        return self.save_data_object
    
    def load_save_data(self, save_number: int):
        """Loads the save as current_save_data, and returns it."""
        self.save_data_object = self.save_manager.load_save(save_number)
        return self.save_data_object
    

    def set_current_page(self, page, a):
        """Set the current page and init it."""

        self.current_page = page
        #print(self.current_page)

        
        #self.current_page = OptionsMenu
        #self.current_page(self)
        return page, a
    

    def exit_game(self):
        """Exit the game."""
        sys.exit()


    def print_message(self):
        """Print message into the terminal."""
        print("message")

