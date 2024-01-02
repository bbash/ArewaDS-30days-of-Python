# 9-1 Restaurant
class Restaurant:
    """A class to model a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('This restaurant is located in Kano')
        print('They have both local and international dishes')

    def open_restaurant(self):
        print('The restaurant is Open')

# instance of the class
restaurant = Restaurant('Dico', 'MMM')

# printing attributes
print(f"The name of the restaurant is {restaurant.restaurant_name}.")
print(f"The cuisine type is {restaurant.cuisine_type}")

#printing methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9 -2 Three Restaurant
my_favourite_restaurant = Restaurant('Pepsin Garden', 'HHH')
her_favourite_restaurant = Restaurant('Freezer', 'DDD')
his_favourite_restaurant = Restaurant('Hotpie', 'FFF')

# calling describe method on the three instances
my_favourite_restaurant.describe_restaurant()
her_favourite_restaurant.describe_restaurant()
his_favourite_restaurant.describe_restaurant()

# 9 - 3 Users:
class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name} and {self.age} years old.")

    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}")

# instance of the class
user_1 = User(first_name='sani', last_name='Bello', age=40)
user_2 = User(first_name='Jamil', last_name='Yusuf', age=20)
user_3 = User(first_name='Tanko', last_name='Jamil', age=15)
print()
user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()

# 9 -4 Number Served
class Restaurant:
    """A class to model a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('This restaurant is located in Kano')
        print('They have both local and international dishes')

    def open_restaurant(self):
        print('The restaurant is Open')

    def set_number_served(self, number):
        self.number_served = number

    def incerement_number_served(self, number):
        self.number_served += number


# instance of a class
restaurant2 = Restaurant('Macky', 'GGGG')
print(f"The number of customers served: {restaurant2.number_served}")
restaurant2.number_served = 23
print(f"The number of customers served: {restaurant2.number_served}")
restaurant2.set_number_served(40)
print(f"Using the set_number_served method, the number of customers served: {restaurant2.number_served}")
restaurant2.incerement_number_served(50)
print(f"Using the increment_number_served method, the number of customers served: {restaurant2.number_served}")

# 9 - 5 Login Attempts
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

login_user = User(first_name='Hack', last_name='John', age=30)
login_user.increment_login_attempts()
login_user.increment_login_attempts()
login_user.increment_login_attempts()
login_user.increment_login_attempts()
login_user.increment_login_attempts()
login_user.increment_login_attempts()
login_user.increment_login_attempts()
print(f"The value of login attempt after seven calling: {login_user.login_attempts}")
login_user.reset_login_attempts()
print(f"After calling the reset method: {login_user.login_attempts}")    
print()

# 9 - 6 Ice Cream Stand,using exercise 9 -4

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        if self.flavors:
            for i, flavor in enumerate(self.flavors):
                print(f"{i+1} - {flavor}")
        else:
            print(f"The list of favours is empty")

# instance of a class
ice_cream_stand = IceCreamStand(
                    restaurant_name='Ice Cream Stand',
                    cuisine_type='FFFF',
                    flavors=['A', 'B', 'C', 'D'])

ice_cream_stand.display_flavors()
print()

# 9 - 7 Admin, using 9 - 5
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

# instance of a class
admin = Admin(first_name='Bello',
              last_name='Tukur',
              age=30,
              privileges=["can add post", "can delete post", "can ban user"])

admin.show_privileges()
print()

# 9 -8 Privileges
class Privileges:

    def __init__(self, privileges=None):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for i, privilege in enumerate(self.privileges):
                print(f"{i+1} - {privilege}")
        else:
            print(f"The privileges list is empty")


class PrivilegeAdmin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


# instance of a class
admin = PrivilegeAdmin(first_name='Bello',
              last_name='Tukur',
              age=30)
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_privileges()
print()

# 9-9 Battery Upgrade
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_batter(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)    
my_tesla.battery.get_range()
my_tesla.battery.upgrade_batter()
my_tesla.battery.get_range()
print()

# 9 - 10 Imported Restaurant done (restaurant.py and test_restaurant.py)

# 9 - 11 Imported Admin done (privileges.py and test_privileges.py)

# 9 - 12 Multiple Module (user.py, privileges_admin.py and test_user.py)

# 9 - 13: Dice
from random import randint
class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

# instance of a class
die_six_sides = Die()
for _ in range(10):
    print(f'Six sides: {die_six_sides.roll_die()}')

die_ten_sides = Die(10)
for _ in range(10):
    print(f'Ten sides: {die_ten_sides.roll_die()}')

die_twenty_sides = Die(20)
for _ in range(10):
    print(f'Twnety sides: {die_twenty_sides.roll_die()}')
print()

# 9 - 14 Lottery
from random import choice
lst = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E']
store = ''
for _ in range(4):
    store += choice(lst)
print(f"Any ticket matching this ticket -- {store} -- wins a prize")
print()
# 9 - 15 Lottery Analysis

count = 0
while True:
    my_ticket = ''
    for _ in range(4):
        my_ticket += choice(lst)
    print(f"my ticket number is {my_ticket}")

    if my_ticket == store:
        print(f"my ticket {my_ticket} and win ticket {store}")
        break
    count += 1
    print(count)

# 9 - 16: Python Module of the Week