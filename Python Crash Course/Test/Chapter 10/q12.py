# 10-12 记住喜欢的数字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字
# 并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
import json

try:
    with open("f_number.txt") as read_num:
        num = json.load(read_num)
except FileNotFoundError:
    number = input("Please enter your favourite number: ")
    with open("f_number.txt", "w") as fnum:
        json.dump(number, fnum)
else:
    print("I know your favorite number! It's " + str(num) + ".")