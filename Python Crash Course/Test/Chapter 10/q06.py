# 10-6 加法运算 ：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入转换为
# 整数时，将引发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时
# 都捕获TypeError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")
first_number = input("\nFirst number: ")
try:
    first = int(first_number)
except ValueError:
    print("Wrong format, you need type arabic numerals.")
else:
    second_number = input("Second number: ")
    try:
        second = int(second_number)
    except ValueError:
        print("Wrong format, you need type arabic numerals.")
    else:
        print(first+second)