# 9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
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


restaurant = Restaurant("Elf kitchen", "Chinese")
restaurant_noodle = Restaurant("Elf noodle", "Chinese")
restaurant_cooker = Restaurant("Elf cooker", "Chinese")
restaurant.discribe_restaurant()
restaurant_noodle.discribe_restaurant()
restaurant_cooker.discribe_restaurant()