"""a module of restaurant"""

class Restaurant():
    """information of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """reset the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def discribe_restaurant(self):
        """show information of restaurant"""
        print("The " + self.cuisine_type.title() + " restaurant's name is " + self.restaurant_name.title() + ".")


    def open_restaurant(self):
        """show the status of restaurant"""
        print("The restaurant " + self.restaurant_name.title() + " is open.")