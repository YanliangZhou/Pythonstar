#coding=utf-8

def p5(n):
    '''combination'''
    List = []
    for g in range(1, n + 1):
        for h in range( 1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    for k in range(1, n + 1):
                        if len(set((g, h, i, j, k))) == 5:  # 去重后长度仍为3的话说明i,j,k的值都不相同
                            one = 'Z'+str(g)
                            two = 'Z'+str(h)
                            three = 'Z'+str(i)
                            four = 'Z'+str(j)
                            five = 'Z'+str(k)
                            l = ','.join(list((one, two, three,four,five)))
                            List.append(l)
    List.append('')
    # finallist = ','.join(List)
    return List

if __name__ == "__main__":
    p = p5(5)
    print(p)




def p6(n):
    '''combination'''
    List = []
    for g in range(1, n + 1):
        for h in range( 1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    for k in range(1, n + 1):
                        for m in range(1, n + 1):
                            if len(set((g, h, i, j, k, m))) == 6:  # 去重后长度仍为3的话说明i,j,k的值都不相同
                                one = 'Z'+str(g)
                                two = 'Z'+str(h)
                                three = 'Z'+str(i)
                                four = 'Z'+str(j)
                                five = 'Z'+str(k)
                                six = 'Z' + str(m)
                                l = ','.join(list((one, two, three, four, five, six)))
                                List.append(l)
    List.append('')
    # finallist = ','.join(List)
    return List

if __name__ == "__main__":
    p = p6(6)
    print(p)