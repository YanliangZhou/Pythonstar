# 9-7 管理员 ：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加一个名为
# privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。编写一个
# 名为show_privileges() 的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。
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

class Admin(User):
    """Admin"""
    def __init__(self, first_name, last_name, age):
        """reset"""
        super().__init__(first_name, last_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """show privileges"""
        print("You are an administrator, you " + self.privileges[0] + ", " + self.privileges[1] + ", " + self.privileges[2] + ".")



user1 = Admin("Yanliang", "Zhou", 29)
user1.describe_user()
user1.greet_user()
user1.show_privileges()