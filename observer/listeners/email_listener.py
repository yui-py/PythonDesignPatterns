from typing import Text, Union, Any
from observer.listeners.event_listeners import EventListener


class EmailListener(EventListener):

    def update(self, message: Union[Text, Any]) -> None:
        print(f"[{self.__class__.__name__}] is updating: {str(message)}")
