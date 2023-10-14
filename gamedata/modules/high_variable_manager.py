from save_manager import SaveManager

class VariableManager:
    """The class that manages the modification of important variables such as health of actors and points."""

    def __init__(self) -> None:
        
        # Load an instance of SaveManager
        self.save_manager = SaveManager()
