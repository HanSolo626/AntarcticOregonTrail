import random

class Event:
    """The parent class for all event types. Made up of Statement objects."""

    def __init__(self) -> None:

        self.statement_list = []
        self.current_statement = 0

    def get_statement(self, statement_number: int):
        """Return a specific statement with it's index number."""
        try:
            return self.statement_list[statement_number]
        except IndexError:
            return "<No statement found.>"
    
    def get_statement_list(self):
        """Return the full list of statements."""
        return self.statement_list
    
    def set_statement_list(self, statement_list: list):
        """Redefine the statement list."""
        self.statement_list = statement_list


# Put new Event objects between Event and RandomEvent


class RandomEvent(Event):
    """Acts as a random event from the list inputed."""

    def __init__(self, option_list: list[Event]) -> None:
        super().__init__()

        # Pick a random Event object from the option list.
        self.selected_event = option_list[random.randint(0, option_list.__len__())]

        return self.selected_event()
    


