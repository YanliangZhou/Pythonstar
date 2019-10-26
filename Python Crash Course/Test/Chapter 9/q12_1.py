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