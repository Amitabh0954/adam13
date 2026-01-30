# Epic Title: User Account Management

class Profile:
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, preferences: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.preferences = preferences

    @staticmethod
    def validate_email(email: str) -> bool:
        import re
        return re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email) is not None