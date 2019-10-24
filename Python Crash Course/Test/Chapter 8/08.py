# 8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用
# 函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
def make_album(name, album, num=''):
    """information of singer"""
    information = {"Name": name, "Album": album}
    if num:
        information["Num"] = num
    return information


while True:
    print("\nPlease tell me the singer's information:")
    print("(enter 'q' at any time to quit)")
    input_name = input("Name: ")
    if input_name == "q":
        break
    input_album = input("Album ")
    if input_album == "q":
        break
    info = {"Name": input_name, "Album": input_album}
    print(info)