# 9-3 用户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在
# 类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出
# 个性化的问候。创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    """discribe User"""
    def __init__(self, first_name, last_name, age):
        """user's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        """discribe"""
        print("The User " + self.first_name.title() + " " +  self.last_name.title() + " is " + str(self.age)
              + " years old.")


    def greet_user(self):
        """greet"""
        print("Good morning, " + self.first_name.title() + " " +  self.last_name.title() + ".")


user1 = User("Yanliang", "Zhou", 29)
user2 = User("Mingli", "Zhang", 20)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()