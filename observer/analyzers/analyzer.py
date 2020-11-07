from observer.event_manager import EventManager


class Analyzer:
    def __init__(self):
        self.events = EventManager()

    def do_something(self):
        print(f"[{self.__class__.__name__}] I'm doing something important.")
        self.events.notify(event_type="test", message="Something has just updated")
