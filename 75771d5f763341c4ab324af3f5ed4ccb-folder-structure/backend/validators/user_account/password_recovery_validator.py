# Epic Title: Password Recovery

class PasswordRecoveryValidator:
    def __init__(self, data: dict, is_reset: bool = False):
        self.data = data
        self.is_reset = is_reset
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        if self.is_reset:
            self.check_token()
            self.check_new_password()
        else:
            self.check_email()
        return len(self.errors) == 0

    def check_email(self):
        email = self.data.get('email', '')
        if not email or '@' not in email:
            self.errors.append("Invalid email format.")
    
    def check_token(self):
        token = self.data.get('token', '')
        if not token:
            self.errors.append("Invalid token.")

    def check_new_password(self):
        new_password = self.data.get('new_password', '')
        if not new_password or len(new_password) < 8:
            self.errors.append("New password must be at least 8 characters long.")