"""a module of privileges"""

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