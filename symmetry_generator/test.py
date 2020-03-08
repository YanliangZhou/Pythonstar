a = ["1","11","2","111"]
#b=sorted(a,key=lambda d:int(d))
b = [int(x) for x in a]
b=sorted(b,key=lambda d:int(d))
print(b)
print(b)