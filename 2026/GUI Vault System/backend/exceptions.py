class AuthError(Exception):
    """Base class for all authentication errors."""
    pass

class UserAlreadyExists(AuthError):
    """Raised when trying to register a username that already exists."""
    pass

class InvalidCredentials(AuthError):
    """Raised when login credentials are invalid."""
    pass

class MissingCredentials(AuthError):
    """Raised when missing username/password"""
    pass

class ErrorWritingToJson(AuthError):
    """Raised when error writing to the json"""
    pass



class VaultError(Exception):
    """Base class for all vault errors."""
    pass

class VaultDoesntExist(VaultError):
    """Raised when vault doesnt exist for user."""
    pass

class FileAlreadyExists(VaultError):
    """Raised when user tries to upload a file that already exists."""
    pass

class ErrorCopyingFile(VaultError):
    """Raised when random error uploading file. Check log for more info"""
    pass 

class FileNotExists(VaultError):
    """Raised when trying to delete a file that doesnt exist."""
    pass

class ErrorDeletingFile(VaultError):
    """Raised when error deleting file"""
    pass

class ErrorDownloadingFile(VaultError):
    """Raised when error downloading file."""
    pass

class InvalidDownloadPath(VaultError):
    """Raised when invalid download path for file, shouldn't happen."""
    pass