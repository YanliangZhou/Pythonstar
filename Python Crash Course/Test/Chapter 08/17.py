# 8-17 函数编写指南 ：选择你在本章中编写的三个程序，确保它们遵循了本节介绍的函数编写指南。
#01
def display_message():
    """didplay what you learn in this chapter"""
    print("I learn how to define a function in this chapter.")


display_message()

#02
def favorite_book(title):
    """display my favorite book"""
    print("One of my favorite books is " + title.title() + ".")


favorite_book("Python Crash Course")

#10
names = ['A', 'B', 'C']
newnames = []


def make_great(names):
    """make great"""
    for name in names:
        newname = "the Great " + name
        newnames.append(newname)


def show_magicians(newnames):
    """show magicians' name"""
    for name in newnames:
        print(name)


make_great(names)
show_magicians(newnames)