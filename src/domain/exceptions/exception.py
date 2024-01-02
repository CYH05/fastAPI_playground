class AbstractBaseException(Exception):
    status: int
    message: str
    
    def __init__(self, status: int, message: str) -> None:
        self.status = status
        self.message = message        

class InvalidDataFormatException(AbstractBaseException):
    pass

class MissingDataException(AbstractBaseException):
    pass
    
class DuplicatedRegisterException(AbstractBaseException):
    pass