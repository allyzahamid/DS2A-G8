from statistics import mean, median, mode, variance, stdev
from ..core.statistical_method import StatisticalMethod
from ..core.data_validator import DataValidator

class DescriptiveStatistics(StatisticalMethod):
    """Perform descripive statistical calculations."""

    def __init__(self):
        """Initialize the descriptive statistics class."""
        super().__init__()
        self.__validator = DataValidator()

    def calculate(self, data):
        """Calculate the mean of the given data."""
        return self.calculate_mean(data)