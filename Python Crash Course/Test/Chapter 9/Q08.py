# 9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法
# show_privileges() 移到这个类中。在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法
# show_privileges() 来显示其权限。
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


user = Admin("Yanliang", "Zhou")
user.privilege.show_privileges()