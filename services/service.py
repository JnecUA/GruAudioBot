from db import Database

from services.user_service import UserService


class Services:
    def __init__(self, db: Database) -> None:
        self.userService = UserService(db.get_collection('users'))
