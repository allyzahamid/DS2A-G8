from abc import ABC, abstractmethod

class StatisticalMethod(ABC):
    """Base class for all statistical methods."""

    def __init__(self):
        """Initialize the statistical method."""
        self._name = self.__class__.__name__

    @property
    def name(self):
        """Return the name of the statistical method."""
        return self._name

    @abstractmethod
    def calculate(self, data):
        """Perform a statistical calculation."""
        pass