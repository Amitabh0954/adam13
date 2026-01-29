# Epic Title: Profile Management

class ProfileManagementValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_first_name()
        self.check_last_name()
        return len(self.errors) == 0

    def check_first_name(self):
        first_name = self.data.get('first_name', '')
        if not first_name:
            self.errors.append("First name is required.")
    
    def check_last_name(self):
        last_name = self.data.get('last_name', '')
        if not last_name:
            self.errors.append("Last name is required.")