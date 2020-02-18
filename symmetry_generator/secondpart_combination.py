#coding=utf-8

def c3(n):
    '''permutation'''
    list = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                list.append(i*100+j*10+k)
                list[-1] = 'X' + str(list[-1])
    # finallist = ','.join(list)
    return list

if __name__ == "__main__":
    c = c3(5)
    print(c)




def c2(n):
    '''permutation'''
    list = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
                list.append(i*10+j)
                list[-1] = 'X' + str(list[-1])
    # finallist = ','.join(list)
    return list

if __name__ == "__main__":
    c = c2(5)
    print(c)




def c1(n):
    '''permutation'''
    list = []
    for i in range(1,n+1):
                list.append(i)
                list[-1] = 'Y' + str(list[-1])
    # finallist = ','.join(list)
    return list

if __name__ == "__main__":
    c = c1(9)
    print(c)