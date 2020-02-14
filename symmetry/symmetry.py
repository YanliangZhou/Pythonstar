# coding：utf-8

from firstpart_permutation import p
from secondpart_combination import c
from multiple_replace import multiple_replace

Znum = 5
Xlenth = 3
total = 64
M = 3 * Znum
p = p(5)
c = c(5)
count = 0
lenth = 0
casenum = 0
output = []
Output = []
sort1 = []
sortedlist = []
SSortedlist = []
com = []
Combination = []
l1 = [p[0]]  # 选取Z第一行
f1 = l1 + c  # 合并成完整第一行
F1 = ','.join(f1)  # 消去符号
C = ','.join(c)  # 消符号
L = ','.join(l1)  # 消符号
P = ','.join(p)  # 消符号
Ppart = [P[q: q + M] for q in range(0, len(P), M)]  # P分块
# print(Ppart)
for g, h, i, j, k in zip(P[1::15], P[4::15], P[7::15], P[10::15], P[13::15]):
    list1 = []
    adict = {
        str(P[1]): g,
        str(P[4]): h,
        str(P[7]): i,
        str(P[10]): j,
        str(P[13]): k,
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
        sortedlist = 'X' + str(sortedlist) + ''
        Sortedlist.append(sortedlist)
        # Sort.append(',')
        # print(str(sortedlist))
    SSortedlist.append(Sortedlist)

        # print(Sort)
        # list(Sort).sort()
        # Sort = 'X' + str(Sort)
        # sortedlist = slist.split()
        # sortedlist.sort()
        # sortedlist = ''.join(sortedlist)
        # sortedlist = 'X' + str(sortedlist) + ''
        # print(Sort)
        # Sortedlist.append(sortedlist)
    # print(Sortedlist)
    count += 1

count = 0
# print(SSortedlist[0])
# SSortedlistpart = [SSortedlist[q: q + M] for q in range(0, len(SSortedlist), M)]  # SSortedlist分块
    # SortedList.append(Sortedlist)
# print(SortedList)
for times in SSortedlist:
    # ssortedlist = ''.join(str(SSortedlist))
    # print(ssortedlist)
    ssortedlist = ','.join(SSortedlist[count])
    combination = 'W,' + Ppart[count] + ssortedlist
    # list(combination).append('\n')
    com.append(combination)
    # ssortedlist = ''.join(Combination)
    count += 1

# com = str(Combination).split('\n')
count = 0
Com = ''.join(com)
# COM = list(Com)
print(Com[0])
print(com)
# print(Combination)
'''排序'''
# print(Output)
file = open('Symmetry','w')

for row in com:
    file.write(str(com[count])+'\n')
    count += 1

count = 0
file.close()
print("Saved Successfully")
