# 9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
# 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出
# 餐馆正在营业。根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
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
restaurant.discribe_restaurant()
restaurant.open_restaurant()