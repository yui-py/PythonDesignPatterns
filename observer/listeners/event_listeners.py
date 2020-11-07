from abc import ABC, abstractmethod
from typing import Text, Union, Any


class EventListener(ABC):
    """
    The subscriber declares the update method
    """

    @abstractmethod
    def update(self, message: Union[Text, Any]) -> None:
        """
        Receive update from analyzer.
        """
        pass
