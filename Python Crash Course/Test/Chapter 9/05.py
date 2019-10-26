# 9-5 尝试登录次数 ：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为
# increment_login_attempts() 的方法，它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，
# 它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；
# 然后，调用方法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
    """discribe User"""
    def __init__(self, first_name, last_name, age):
        """user's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """discribe"""
        print("The User " + self.first_name.title() + " " +  self.last_name.title() + " is " + str(self.age)
              + " years old.")


    def greet_user(self):
        """greet"""
        print("Good morning, " + self.first_name.title() + " " +  self.last_name.title() + ".")


    def increment_login_attempts(self):
        """increment"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """reset"""
        self.login_attempts = 0


user1 = User("Yanliang", "Zhou", 29)
user1.increment_login_attempts()
print("The number of login_attempts is " + str(user1.login_attempts))
user1.increment_login_attempts()
print("The number of login_attempts is " + str(user1.login_attempts))
user1.reset_login_attempts()
print("The number of login_attempts is " + str(user1.login_attempts))