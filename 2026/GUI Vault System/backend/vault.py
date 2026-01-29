from pathlib import Path
import logging
import shutil

from backend.exceptions import (
    VaultDoesntExist,
    FileAlreadyExists,
    FileNotExists,
    ErrorCopyingFile,
    ErrorDeletingFile,
    ErrorDownloadingFile,
    InvalidDownloadPath
)

class VaultManager:
    def __init__(self):
        self.vault_location = Path(__file__).resolve().parent.parent / "data" / "vaults"

    def _get_user_vault(self, username: str) -> Path:
        user_vault = self.vault_location / username
        if not user_vault.exists():
            logging.error(f"BACKEND - vault.py - Vault doesn't exist for '{username}'")
            raise VaultDoesntExist(f"Vault for user '{username}' does not exist.")
        return user_vault
    # End function

    def view_all_files(self, username: str):
        user_vault = self._get_user_vault(username)
        return [f.name for f in user_vault.iterdir() if f.is_file()]
    # End function

    def upload_file(self, username: str, file_to_upload_path: str):
        user_vault = self._get_user_vault(username)
        source = Path(file_to_upload_path).resolve()

        destination = (user_vault / source.name).resolve()

        if user_vault not in destination.parents:
            raise ErrorCopyingFile("Invalid file destination.")

        if destination.exists():
            logging.warning(f"BACKEND - vault.py - '{username}' tried to upload file that already exists.")
            raise FileAlreadyExists(f"{source.name} already exists.")

        try:
            shutil.copy2(source, destination)
            logging.info(f"BACKEND - vault.py - File {source.name} copied to {destination}")
        except Exception as e:
            logging.error(f"BACKEND - vault.py - Error copying file {source.name} for {username}")
            raise ErrorCopyingFile(e)

        return f"{source.name} uploaded successfully!"
    # End function

    def delete_file(self, username: str, file_to_delete: str):
        user_vault = self._get_user_vault(username)
        target = (user_vault / file_to_delete).resolve()

        if user_vault not in target.parents:
            raise ErrorDeletingFile("Invalid file path.")

        if not target.exists():
            logging.warning(f"BACKEND - vault.py - File {file_to_delete} does not exist in {username}'s vault.")
            raise FileNotExists(f"{file_to_delete} does not exist in your vault.")

        try:
            target.unlink()
            logging.info(f"BACKEND - vault.py - Deleted file {file_to_delete} for user '{username}'")
        except Exception as e:
            logging.error(f"BACKEND - vault.py - Error deleting file {file_to_delete} for {username}")
            raise ErrorDeletingFile(e)

        return f"{file_to_delete} deleted successfully!"
    # End function

    def download_file(self, username: str, file_to_download: str, download_path: str):
        user_vault = self._get_user_vault(username)
        target = (user_vault / file_to_download).resolve()

        download_location = Path(download_path)

        if user_vault not in target.parents:
            raise ErrorDownloadingFile("Invalid file path.")
        
        if not target.exists():
            logging.warning(f"BACKEND - vault.py - File {file_to_download} does not exist in {username}'s vault.")
            raise FileNotExists(f"{file_to_download} does not exist in your vault.")
    
        if not download_location.is_dir():
            logging.warning(f"BACKEND - vault.py - Invalid path to download to. {download_path}")
            raise InvalidDownloadPath(f"{download_path} is not a valid download path.")
        
        try:
            shutil.copy2(target, download_location)
            logging.info(f"BACKEND - vault.py - File {file_to_download} downloaded by {username}")
        except Exception as e:
            logging.error(f"BACKEND - vault.py - Error downloading file {file_to_download} for {username}")
            raise ErrorDownloadingFile(e)
        
        return f"{file_to_download} downloaded to {download_path} successfully!"
    # End function