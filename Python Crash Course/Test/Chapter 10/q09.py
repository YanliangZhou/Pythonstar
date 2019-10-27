# 10-9 沉默的猫和狗 ：修改你在练习10-8中编写的except 代码块，让程序在文件不存在时一言不发。
def show_name(filename):
    """show name"""
    try:
        with open(filename) as animal_object:
            names = animal_object.readlines()
    except FileNotFoundError:
        pass
    else:
        for name in names:
            print(name.strip())

filenames = ["cats.txt", "dog.txt"]
for filename in filenames:
    show_name(filename)