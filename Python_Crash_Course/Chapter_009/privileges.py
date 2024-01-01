class User:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name} and {self.age} years old.")
        
    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        


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
        
        