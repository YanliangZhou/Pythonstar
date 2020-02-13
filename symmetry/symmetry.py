# coding：utf-8

from firstpart_permutation import p
from secondpart_combination import c
from multiple_replace import multiple_replace

M=15
p = p(5)
c = c(5)
count = 0
output = []
Output = []
Sort = []
l1 = [p[0]]   # 选取Z第一行
f1 = l1+c     # 合并成完整第一行
F1 = ','.join(f1)     # 消去符号
C = ','.join(c)    # 消符号
L = ','.join(l1)    # 消符号
P = ','.join(p)    # 消符号
Ppart = [P[q : q + M] for q in range(0, len(P), M)]     # P分块

for g, h, i, j, k in zip(P[1::15], P[4::15], P[7::15], P[10::15], P[13::15]):
    list = []
    adict = {
        str(P[1]): g,
        str(P[4]): h,
        str(P[7]): i,
        str(P[10]): j,
        str(P[13]): k,
    }
    list.append(multiple_replace(C, adict))
    List = ','.join(list)
    comb = Ppart[count]+List
    output.append(comb)
    count += 1

count = 0

for a in output:
    if count == 0:
        Output = a
        count += 1
    else:
        Output=str(Output) + a
        count += 1
count = 0
print(Output[0])
a = Output
n = 64
CC= [a[i:i+n] for i in range(0, len(a), n)]
print(CC)
print(CC[0])
for b in CC:
    cc = CC[count]
'''排序'''
# print(Output)
# file = open('Symmetry','a')
# file.write(Output)
# file.close()
# print("Saved Successfully")