# 7-10 梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world, where
# would you go?”的提示，并编写一个打印调查结果的代码块。
question = "If you could visit one place in the world, where would you go? "
question += "\nEnter 'quit' to quit the survey."
answer = ""
place = []
while answer != "quit":
    answer = input(question)
    if answer != "quit":
        print(answer)
        place.append(answer)
print("Lily wants to go to the following places: ")
for i in place:
    print("\t" + i)