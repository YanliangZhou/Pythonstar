# 11-3 雇员 ：编写一个名为Employee 的类，其方法__init__() 接受名、姓和年薪，并将它们都存储在属性中。编写一个名为give_raise()
# 的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。为Employee 编写一个测试用例，其中包含两个测试方法：
# test_give_default_raise() 和test_give_custom_raise() 。使用方法setUp() ，以免在每个测试方法中都创建新的雇员实例。
# 运行这个测试用例，确认两个测试都通过了。
import unittest

class Employee():
    """show the salary"""
    def __init__(self, first_name, last_name):
        """reset"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 80000


    def give_raise(self, raise_salary=5000):
        """raise salary"""
        self.salary += raise_salary

# employee = Employee("Yanliang", "Zhou")
# # employee.give_raise(10000)
# # print(int(employee.salary))

class Raise_salary(unittest.TestCase):
    """test raise salary"""
    def setUp(self):
        """set an object"""
        self.employee = Employee("Yanliang", "Zhou")


    def test_give_default_raise(self):
        """test default raise"""
        self.employee.give_raise()
        self.assertEqual(int(self.employee.salary), 85000)


    def test_give_custom_raise(self):
        """test custom raise"""
        self.employee.give_raise(10000)
        self.assertEqual(int(self.employee.salary), 90000)

if __name__== '__main__':
    """In pycharm, We need add this code here:if __name__== '__main__':."""
    unittest.main()
