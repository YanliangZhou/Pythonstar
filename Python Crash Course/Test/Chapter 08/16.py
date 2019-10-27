# 8-16 导入 ：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，
# 再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# import city_information
# city = city_information.city_country("Wuhan", "China")
# print(city)


# from city_information import city_country
# city = city_country("Wuhan", "China")
# print(city)


# from city_information import city_country as c
# city = c("Wuhan", "China")
# print(city)


# import city_information as c
# city = c.city_country("Wuhan", "China")
# print(city)

from city_information import *
city = city_country("Wuhan", "China")
print(city)