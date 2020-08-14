# # for i in range(10):
# #     exec('a%s=%d'%(i, i))
# # for i in range(10):
# #     exec('print(a%s)'%i)
#
# import numpy as np
#
#
# def fun(n, in_list, state, out_list):
#     num = n
#     if (n == 0):
#         print(out_list)
#     else:
#         for i in range(len(in_list)):
#             if state[i]:
#                 out_list[n - 1] = in_list[i]
#                 state[i] = False
#                 fun(n - 1, in_list, state, out_list)
#                 state[i] = True
#
#
# def full_permutation(in_list):
#     n = len(in_list)
#     state = [True for _ in range(n)]
#     out_list = in_list.copy()
#     fun(n, in_list, state, out_list)
#
#
# a = np.arange(3).tolist()
# full_permutation(a)
#
# # if __name__ == "__main__":
# #     l = [1,2,3]
# #     result = full_permutation(l)
# #     # print(result)
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
m = fact(995)
print(m)