from gamedata.modules.save_manager import SaveManager
import sys

class VariableManager:
    """The class that manages the modification of important variables such as health of actors and points."""

    def __init__(self) -> None:
        
        # Load an instance of SaveManager
        self.save_manager = SaveManager()


    def get_current_save_data(self):
        """Returns current save object."""
        return self.save_data_object
    
    def load_save_data(self, save_number: int):
        """Loads the save as current_save_data, and returns it."""
        self.save_data_object = self.save_manager.load_save(save_number)
        return self.save_data_object
    

    def exit_game(self):
        """Exit the game."""
        sys.exit()

    def print_message(self):
        """Print message into the terminal."""
        print("message")

