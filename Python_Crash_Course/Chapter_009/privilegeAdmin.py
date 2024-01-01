from user import User

class Privileges:
    
    def __init__(self, privileges=None):
        self.privileges = privileges
        
    def show_privileges(self):
        if self.privileges:
            for i, privilege in enumerate(self.privileges):
                print(f"{i+1} - {privilege}")
        else:
            print(f"The privileges list is empty")
    
    
class Admin(User):
    
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges
        
    def show_privileges(self):
        if self.privileges:
            for i, privilege in enumerate(self.privileges):
                print(f"{i+1} - {privilege}")
        else:
            print(f"The privileges list is empty")
        
        