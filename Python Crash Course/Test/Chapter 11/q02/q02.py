# 11-2 人口数量 ：修改前面的函数，使其包含第三个必不可少的形参population ，并返回一个格式为City, Country - population xxx
# 的字符串，如Santiago, Chile - population 5000000 。运行test_cities.py，确认测试test_city_country() 未通过。
# 修改上述函数，将形参population 设置为可选的。再次运行test_cities.py，确认测试test_city_country() 又通过了。
# 再编写一个名为test_city_country_population() 的测试，核实可以使用类似于'santiago' 、'chile' 和'population=5000000'
# 这样的值来调用这个函数。再次运行test_cities.py，确认测试test_city_country_population() 通过了。
import unittest
from city_functions import city_name

class NamesTestCase(unittest.TestCase):
    """test city_function.py"""
    def test_city_country_name(self):
        """test the format"""
        formatted_name = city_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """test all information"""
        formatted_name = city_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


if __name__== '__main__':
    """In pycharm, We need add this code here:if __name__== '__main__':."""
    unittest.main()