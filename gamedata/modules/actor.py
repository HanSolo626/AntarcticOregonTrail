from image_manager import *

class Actor:
    """The parent class for all Actor types."""

    def __init__(self) -> None:
        
        self.profession = str
        self.description = str

        self.abilities = None

        self.image = None
        self.portrait = None

        self.health = 5
        self.stamina = 5
        self.morale = 5

        self.max_health = 5
        self.max_stamina = 5
        self.max_morale = 5

        self.abilities

    def set_actor(self, new_profession: str, new_desciption: str, new_abilities: str, image: Image, portrait: Image):
        """Set actor stats."""

        self.profession = new_profession
        self.description = new_desciption
        self.abilities = new_abilities
        self.image = image
        self.portrait = portrait

    def set_numbers(self, health, stamina, morale):
        """Set the number stats of the actor."""
        self.health = health
        self.stamina = stamina
        self.morale = morale



    def increase_health(self):
        if not self.health >= self.max_health:
            self.health += 1
    
    def decrease_health(self):
        if not self.health <= 0:
            self.health -= 1

    def increase_stamina(self):
        if not self.stamina >= self.max_stamina:
            self.stamina += 1

    def decrease_stamina(self):
        if not self.stamina <= 0:
            self.stamina -= 1

    def increase_morale(self):
        if not self.morale >= self.max_morale:
            self.morale += 1

    def decrease_morale(self):
        if not self.morale <= 0:
            self.morale -= 1

    
    def increase_max_health(self):
        self.max_health += 1

    def decrease_max_health(self):
        if not self.max_health <= 0:
            self.max_health -= 1

    def increase_max_stamina(self):
        self.max_stamina += 1

    def decrease_max_stamina(self):
        if not self.max_stamina <= 0:
            self.max_stamina -= 1

    def increase_max_morale(self):
        self.max_morale += 1

    def decrease_max_morale(self):
        if not self.max_morale <= 0:
            self.max_stamina -= 1



    def get_actor_traits(self):
        """Get actor traits in a list format."""
        return [self.profession, self.description, self.abilities, self.image, self.portrait]
    
    def get_actor_numbers(self):
        """Get actor stats in list format."""
        return [self.health, self.stamina, self.morale] # More will be added to this list.
    




