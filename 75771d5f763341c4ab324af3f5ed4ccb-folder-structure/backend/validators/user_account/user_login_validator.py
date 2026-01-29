# Epic Title: User Login

class UserLoginValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
        
    def is_valid(self) -> bool:
        self.errors = []
        self.check_email()
        self.check_password()
        return len(self.errors) == 0

    def check_email(self):
        email = self.data.get('email', '')
        if not email or '@' not in email:
            self.errors.append("Invalid email format.")
    
    def check_password(self):
        password = self.data.get('password', '')
        if not password or len(password) < 8:
            self.errors.append("Password must be at least 8 characters long.")