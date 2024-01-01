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
    