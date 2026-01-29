import bcrypt
import json
import logging
from pathlib import Path
from backend.exceptions import AuthError, UserAlreadyExists, InvalidCredentials, MissingCredentials, ErrorWritingToJson

class AuthManager:

    def __init__(self):
        self.user_details = {}

        self.users_file = Path(__file__).resolve().parent.parent / "data" / "users.json"

        self.users_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.users_file.exists():
            try:
                self.users_file.write_text("[]")
            except OSError as e:
                logging.error(f"Failed to create users.json: {e}")

        self.vault_location = Path(__file__).resolve().parent.parent / "data" / "vaults"

        self.vault_location.mkdir(parents=True, exist_ok=True)
    # End function

    def load_details(self):
        with open(self.users_file, 'r') as user_logins:
            try:
                logins = json.load(user_logins)
                logging.info("BACKEND - auth.py - User json loaded successfully.")
            except json.JSONDecodeError as e:
                logging.error(f"BACKEND - auth.py - User json loading failed. {e}")
                logins = []
        
        for user in logins:
            self.user_details[user["username"]] = user["password"]
        
        return self.user_details
    # End function

    def login(self, username, password):
        if not username or not password:
            logging.warning(f"BACKEND - auth.py - Login failed as username or password not provided.")
            raise MissingCredentials("Username and password are required.")

        if username not in self.user_details:
            logging.warning(f"BACKEND - auth.py - Login failed as user does not exist.")
            raise InvalidCredentials("Invalid username or password.")

        hashed_pw = self.user_details[username]
        if not bcrypt.checkpw(password.encode("utf-8"), hashed_pw.encode("utf-8")):
            logging.warning(f"BACKEND - auth.py - Login failed due to invalid password.")
            raise InvalidCredentials("Invalid username or password")

        logging.info(f"BACKEND - auth.py - Successful login attempt for user '{username}'")
        return "Successfuly login!", username
    # End function

    def register(self, username, password):
        if not username or not password:
            logging.warning(f"BACKEND - auth.py - Registration failed as username or password not provided.")
            raise MissingCredentials("Username and password are required.")
        
        if username in self.user_details:
            logging.warning(f"BACKEND - auth.py - Registration failed as user '{username}' already exists.")
            raise UserAlreadyExists("Account already exists with that username.")
        
        pswd = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(pswd, bcrypt.gensalt())

        logging.info(f"BACKEND - auth.py - User '{username}' registered successfully.")
        self.write_to_json(username, hashed_password)
        self.create_user_vault(username)

        return f"{username} registered successfully!"
    # End function

    def write_to_json(self, username, password):
        self.user_details[username] = password.decode("utf-8")
        users_list = [{"username": u, "password": p} for u, p in self.user_details.items()]
        try:
            with open(self.users_file, 'w') as file:
                json.dump(users_list, file, indent=4)
                logging.info("BACKEND - auth.py - New user details written to json.")
        except Exception as e:
            logging.error("BACKEND - auth.py - Error writing to json.")
            raise ErrorWritingToJson("Error writing new user to json.")
    # End function

    def create_user_vault(self, username): 
        user_vault = self.vault_location / username

        try:
            user_vault.mkdir(exist_ok=False)
            logging.info(f"BACKEND - auth.py - Created a vault for {username}, path: 'data/vaults/{username}'")
        except Exception as e:
            logging.error(f"BACKEND - auth.py - Error creating vault for {username}. {e}")
            raise AuthError("Error creating vault.")
    # End function