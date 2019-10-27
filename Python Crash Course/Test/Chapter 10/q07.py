# 10-7 加法计算器 ：将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    try:
        first = int(first_number)
    except ValueError:
        print("Wrong format, you need type arabic numerals.")
        continue
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        second = int(second_number)
    except ValueError:
        print("Wrong format, you need type arabic numerals.")
        continue
    else:
        print(first+second)