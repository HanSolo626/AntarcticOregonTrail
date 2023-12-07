# THE HIGH VARIABLE MANAGER #

# Pages are defined here.








from gamedata.modules.save_manager import SaveManager
from gamedata.modules.button import *
from gamedata.modules.page import *

import sys



############################
### HIH VARIABLE MANAGER ###
############################

class VariableManager:
    """The class that manages the modification of important variables such as health of actors and points."""

    def __init__(self, ai_game) -> None:
        
        # Load an instance of SaveManager
        self.save_manager = SaveManager()


        self.current_page = None

        if ai_game != None:
            self.current_page = HomeMenu(ai_game)


        self.ai_game = ai_game




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
    

    def set_current_page(a, page):
        """Set the current page and init it."""
        print(a)

        def func(self):
            a.hvm.current_page = page(a)
            # init buttons
            a.hvm.current_page.set_button_list(a.hvm.current_page.button_list)
            print(a.hvm.current_page.button_list[0].normal_image)
            return None
        #print(self.current_page)
        
        

        
        #self.current_page = OptionsMenu
        #self.current_page(self)
        return func
    

    def exit_game(self):
        """Exit the game."""
        sys.exit()


    def print_message(self):
        """Print 'message' into the terminal."""
        print("message")





##################
##### PAGES ######
##################



class TestPage(Page):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)

        self.set_background(Image("Test Background").return_image())

        self.set_button_list([
            TestButton(VariableManager.print_message, 1600, 600),
            ExitGame(VariableManager.exit_game, 50, 1000)
        ]
            )
        

class HomeMenu(Page):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)

        self.set_background(Image("Test Background").return_image())


        self.set_button_list([
            ExitGame(VariableManager.exit_game, 50, 1000),
            HomeOptions(VariableManager.set_current_page(ai_game, OptionsMenu), 600, 600),
        ])


class OptionsMenu(Page):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)

        self.set_background(Image("Options Background").return_image())

        self.set_button_list([
            ExitGame(VariableManager.exit_game, 50, 1000)
        ])