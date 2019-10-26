class Privileges():
    """show privileges"""
    def __init__(self):
        """reset"""
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """show privileges"""
        print("You are an administrator, you " + self.privileges[0] + ", " + self.privileges[1]
              + ", " + self.privileges[2] + ".")


class Admin():
    """privileges of admin"""
    def __init__(self, first_name, last_name):
        """reset"""
        self.first_name = first_name
        self.last_name = last_name
        self.privilege = Privileges()


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