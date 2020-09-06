# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValidationError(Error):
    """Raised when a user's input does not pass validation"""
    def __init__(self, message="A Validation error has occurred"):
        self.message=message
        super().__init__(self.message)
