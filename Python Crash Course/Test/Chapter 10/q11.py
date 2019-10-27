# 10-11 喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。再编写一个程序，
# 从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。
import json

number = input("Please enter your favourite number: ")
with open("favourite_number.txt", 'w') as fnum:
    json.dump(number, fnum)

with open("favourite_number.txt") as read_num:
    num = json.load(read_num)
    print("I know your favorite number! It's " + str(num) + ".")