class MEngineException(Exception):
    """ Base class for all exceptions within the application """
    pass

class ValidationError(MEngineException):
    """ Exception for validation errors """

    def __init__(self, field, message="Invalid input"):
        self.field = field
        self.message = message
        super().__init__(f"Validation error on '{field}': {message}")

class HTTPException(MEngineException):
    """ Exception for HTTP protocol related errors """
    pass