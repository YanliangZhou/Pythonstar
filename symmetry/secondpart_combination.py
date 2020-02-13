#coding=utf-8

def c(n):
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
    c = c(5)
    print(c)