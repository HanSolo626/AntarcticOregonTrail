from events import *
# Import everything from 'events.py'

class Journey:
    """The parent class for all journeys. Made up of Event objects."""

    def __init__(self) -> None:
        self.event_list = []
        self.current_event = 0

    def get_event(self, event_number: int):
        """Return a specific Event object with it's index number."""
        try:
            return self.event_list[event_number]
        except IndexError:
            return "<No event found.>"
        
    def get_event_list(self):
        """Return the full list of Events."""
        return self.event_list
    
    def set_event_list(self, event_list: list[Event]):
        """Redefine the event list."""
        self.event_list = event_list


class TestJourney(Journey):
    """A test journey to help make other journeys and test stuff."""

    def __init__(self) -> None:
        super().__init__()

        self.set_event_list([TestEvent1, TestEvent2])
