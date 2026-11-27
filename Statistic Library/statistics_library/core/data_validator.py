class DataValidator:
    """Validate numerical data before statistical calculations."""

    def validate_data(self, data):
        """Check if data contains valid numerical values."""

        if not isinstance(data, (list, tuple)):
            raise TypeError("Data must be a list or tuple.")

        if len(data) == 0:
            raise ValueError("Data cannot be empty.")

        for value in data:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("All values must be numbers.0")

            return True
        