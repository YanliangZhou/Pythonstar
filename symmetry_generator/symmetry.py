# coding：utf-8

from firstpart_permutation import p5, p6, p9
from secondpart_combination import c2, c3, c1
from multiple_replace import multiple_replace

Znum = 9
Xlenth = 1
M = 3 * Znum
p = p9(9)
c = c1(9)
total = M + (Xlenth+2) * len(c) - 1
count = 0
lenth = 0
output = []
Output = []
sortedlist = []
SSortedlist = []
com = []
l1 = [p[0]]  # 选取Z第一行
f1 = l1 + c  # 合并成完整第一行
F1 = ','.join(f1)  # 消去符号
C = ','.join(c)  # 消符号
L = ','.join(l1)  # 消符号
P = ','.join(p)  # 消符号
Ppart = [P[q: q + M] for q in range(0, len(P), M)]  # P分块
# print(Ppart)

for g, h, i, j, k, l, m, n, o in zip(P[1::M], P[4::M], P[7::M], P[10::M], P[13::M], P[16::M], P[19::M], P[22::M], P[25::M]):
    list1 = []
    adict = {
        str(P[1]): g,
        str(P[4]): h,
        str(P[7]): i,
        str(P[10]): j,
        str(P[13]): k,
        str(P[16]): l,
        str(P[19]): m,
        str(P[22]): n,
        str(P[25]): o,
    }
    list1.append(multiple_replace(C, adict))
    List = ','.join(list1)
    comb = Ppart[count] + List
    output.append(comb)
    count += 1

# print(output)
count = 0

for a in output:
    if count == 0:
        Output = a
        count += 1
    else:
        Output = str(Output) + a
        count += 1

# print(output)
count = 0
# print(Output[0])
a = Output
# print(a)
CC = [a[i:i + total] for i in range(0, len(a), total)]
# print(CC)
# print(CC[0])

for b in CC:
    cc = CC[count] + ','
    casenum = (len(cc) - M) // (2 + Xlenth)
    # print(casenum)
    Sortedlist = []
    for num in range(casenum):
        # print(num)
        slist = cc[num * (Xlenth + 2) + M + 1:num * (Xlenth + 2) + Xlenth + M + 1]
        # print(slist)
        Sort = []
        for v in slist:
            fir = slist[lenth]
            Sort += fir
            lenth += 1
        lenth = 0
        sortedl = [str(x) for x in Sort]
        sortedl = sorted(sortedl, key=lambda d: int(d))
        sortedlist = ''.join(list(sortedl))
        sortedlist = 'Y' + str(sortedlist) + ''
        Sortedlist.append(sortedlist)
        # print(str(sortedlist))
    SSortedlist.append(Sortedlist)
    count += 1

count = 0

for times in SSortedlist:
    ssortedlist = ','.join(SSortedlist[count])
    combination = Ppart[count] + ssortedlist + ',S'
    com.append(combination)
    count += 1

count = 0
Com = ''.join(com)

file = open('Symmetry','w')

for row in com:
    file.write(str(com[count])+'\n')
    count += 1

count = 0
file.close()
print("Saved Successfully")
