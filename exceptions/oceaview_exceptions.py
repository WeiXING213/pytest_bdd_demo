class OceaViewException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class OceaViewUserNotFoundException(OceaViewException):
    pass

class OceaViewInvalidCredentialException(OceaViewException):
    pass