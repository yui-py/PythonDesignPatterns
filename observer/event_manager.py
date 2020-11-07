from typing import Text
from observer.listeners.event_listeners import EventListener


class EventManager:
    def __init__(self):
        self._listeners = {}
        # Dict of listeners which categorized by event type

    def subscribe(self, event_type: Text, listener: EventListener) -> None:
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: Text, listener: EventListener) -> None:
        if event_type not in self._listeners:
            raise ValueError("{} is not valid".format(event_type))

        self._listeners[event_type].remove(listener)

    def notify(self, event_type: Text, message) -> None:
        """
        Trigger an update in each subscriber.
        """
        if event_type not in self._listeners:
            raise ValueError("{} is not valid".format(event_type))

        event_listeners = self._listeners[event_type]
        for listener in event_listeners:
            listener.update(message)
