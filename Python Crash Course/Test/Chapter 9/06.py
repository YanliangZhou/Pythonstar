# 9-6 冰淇淋小店 ：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的
# Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种
# 口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。
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


class IceCreamStand(Restaurant):
        """IceCream"""
        def __init__(self,restaurant_name, cuisine_type):
            """reset"""
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = ["vanilla icecream", "chocolate icecream"]


        def flavor(self):
            """show the flavors"""
            print("This restaurant has " + self.flavors[0] + ", " + self.flavors[1] + ".")


restaurant = IceCreamStand("Elf kitchen", "Chinese")
restaurant.discribe_restaurant()
restaurant.flavor()