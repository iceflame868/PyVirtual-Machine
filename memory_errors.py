class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class MemoryAccessViolation(Error):
    """
    All read or write access violations will come from here
    """
    def __init__(self, location, message, violation_type):
        """

        :param location: The location in memory where the access violation happened
        :param violation_type: either read or write
        :param message: the reason for
        """
        self.violation_type = violation_type
        self.location = location
        self.message = message


class ReadViolation(MemoryAccessViolation):
    """
    This is for reading memory that we either arent allowed to read, or an overflow of a sort
    """
    def __init__(self, location, message):
        """

        :param location:
        :param message:
        """
        super().__init__(self, location, message)
        self.violation_type = 'Read'


class WriteViolation(MemoryAccessViolation):
    """
    This is for when we write to memory that we dont have permisson to use, or some other type of error
    """

    def __init__(self, location, message):
        """

        :param location:
        :param message:
        """
        super().__init__(self, location, message)
        self.violation_type = 'Write'
