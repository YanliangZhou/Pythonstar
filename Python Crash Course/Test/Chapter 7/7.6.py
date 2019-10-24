# 7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
#   在while 循环中使用条件测试来结束循环。
#   使用变量active 来控制循环结束的时机。
#   使用break 语句在用户输入'quit' 时退出循环。
prompt = "\nPlease enter the ingredients for pizza you want:"
prompt += "\n(Enter 'quit' when you are finished.) "
active = True
while active:
    ingredients = input(prompt)
    if ingredients == 'quit':
        break
    else:
        print("I'll add " + ingredients.title() + " in pizza!")