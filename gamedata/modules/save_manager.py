class SaveObject:
    """Object that holds all the save data."""

    def __init__(self, save_list: list[str]) -> None:
        
        # JOURNEY STATUS
        self.journey_type = save_list[0]
        self.journey_stage = save_list[1]
        self.event_segment = save_list[2]
        
        # ACTOR 1 STATUS
        self.actor1_exists = save_list[3]
        self.actor1_health = save_list[4]
        self.actor1_morale = save_list[5]
        self.actor1_stamina = save_list[6]
        self.ailments = save_list[7]

        # ACTOR 2 STATUS
        self.actor2_exists = save_list[8]
        self.actor2_health = save_list[9]
        self.actor2_morale = save_list[10]
        self.actor2_stamina = save_list[11]
        self.ailments = save_list[12]

        # ACTOR 3 STATUS
        self.actor3_exists = save_list[13]
        self.actor3_health = save_list[14]
        self.actor3_morale = save_list[15]
        self.actor3_stamina = save_list[16]
        self.ailments = save_list[17]

        # ACTOR 4 STATUS
        self.actor4_exists = save_list[18]
        self.actor4_health = save_list[19]
        self.actor4_morale = save_list[20]
        self.actor4_stamina = save_list[21]
        self.ailments = save_list[22]

        # INVENTORY STATUS
        self.food_type1_amount = save_list[23]
        self.food_type2_amount = save_list[24]
        self.inventory = save_list[25]



class SaveManager:
    """The class that manages the saving and modification of save_files."""

    def __init__(self) -> None:
        
        self.save1_name = "save1"
        self.save2_name = "save2"
        self.save3_name = "save3"
        self.save_reset_name = "save_reset"

        self.save_path = "OregonTrail/gamedata/saves/"

        self.current_save = self.load_save(0)
        print(self.current_save)


    def get_save_data(self, save):
        """"""

    def load_save(self, save_number: int):
        """Load the save with the inputed number."""
        
        # Open the file for reading and then close it.
        with open(self.get_save_name(save_number), 'r') as file:
            save = file.readlines()

        # Remove the newline suffixes.
        for value in range(self.current_save.__len__()):
            save[value] = save[value].removesuffix("\n")

        return SaveObject(save)


    def reset_save(self, save_number: int):
        """Reset the save with the inputed number."""

        # Open the reset file.
        with open(self.get_save_name(save_number), 'r') as resetfile:
            
            # Open the save for writing.
            with open(self.get_save_name(0), 'w') as savefile:
                # Write to the reset to the file.
                savefile.write(resetfile.read())


    def write_save(self, save_to_write: str, save_number: int):
        """Write to a save."""

        with open(self.get_save_name(save_number), 'w') as file:
            file.write(save_to_write)


    def get_save_name(self, save_number: int):
        """Return the save file path with the inputed save number."""
        a = ""
        if save_number == 1:
            a = self.save1_name
        elif save_number == 2:
            a = self.save2_name
        elif save_number == 3:
            a = self.save3_name
        elif save_number == 0:
            a = self.save_reset_name
        else:
            raise "Invalid Number! "+str(save_number)
        
        return self.save_path+a

SaveManager()