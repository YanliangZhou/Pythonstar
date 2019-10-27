# 10-5 关于编程的调查 ：编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
with open('reason_like_programming.txt', 'w') as file_object:
    while True:
        reason = input("\nPlease tell me why you like programming: " + "\nYou can type 'quit' to quit.")
        if reason != "quit":
            file_object.write(reason + "\n")
        else:
            break