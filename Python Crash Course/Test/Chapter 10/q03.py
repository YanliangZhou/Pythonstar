# 10-3 访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
with open('guest.txt', 'w') as file_object:
    name = input("Please type your name here: ")
    file_object.write(name)