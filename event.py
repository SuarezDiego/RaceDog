class Event:
    """
    Attributes:
        start_date: date
            The date when the event starts
        finish_date: date
            The date when the event ends
        location: str
            The place where the event is
        races: List<Race>
            List of races scheduled for the event
    """
    def __init__(self, start_date, finish_date, location, races):
        self.start_date = start_date
        self.finish_date = finish_date
        self.location = location
        self.races = races