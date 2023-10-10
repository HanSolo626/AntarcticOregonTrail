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
    
    def set_event_list(self, event_list: list):
        """Redefine the event list."""
        self.event_list = event_list
