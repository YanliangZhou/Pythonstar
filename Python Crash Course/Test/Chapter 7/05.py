# 7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用
# 户的年龄，并指出其票价。。
prompt = "\nPlease enter your age:"
while True:
    age = input(prompt)
    age = int(age)
    if age <= 12:
        if age < 3:
            print("Your ticket price is 0.")
        else:
            print("Your ticket price is 10.")
    if age > 12:
        print("Your ticket price is 15.")
    if age == 'quit':
        break
