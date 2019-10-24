# 8-9 魔术师 ：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
names = ['A', 'B', 'C']


def show_magicians(names):
    """show magicians' name"""
    for name in names:
        print(name)


show_magicians(names)
