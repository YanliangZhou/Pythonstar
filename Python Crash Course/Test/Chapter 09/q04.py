# 9-4 就餐人数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为
# restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆
# 每天可能接待的就餐人数。
class Restaurant():
    """information of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """reset the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def discribe_restaurant(self):
        """show information of restaurant"""
        print("The " + self.cuisine_type.title() + " restaurant's name is " + self.restaurant_name.title() + ".")


    def open_restaurant(self):
        """show the status of restaurant"""
        print("The restaurant " + self.restaurant_name.title() + " is open.")


    def set_number_served(self, number):
        """set the served number"""
        self.number_served = number

    def increment_number_served(self, increment):
        """increment"""
        self.number_served += increment


restaurant = Restaurant("Elf kitchen", "Chinese", )
print("The number of served customers is " + str(restaurant.number_served) + ".")
restaurant.number_served = 200
print("The number of served customers is " + str(restaurant.number_served) + ".")
restaurant.set_number_served(300)
print("The number of served customers is " + str(restaurant.number_served) + ".")
restaurant.increment_number_served(50)
print("The number of served customers is " + str(restaurant.number_served) + ".")