# 8-2 喜欢的图书 ：编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，如One of my favorite
# books is Alice in Wonderland 。调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    """display my favorite book"""
    print("One of my favorite books is " + title.title() + ".")
favorite_book("Python Crash Course")