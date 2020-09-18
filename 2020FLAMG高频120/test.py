# class ListNode(object):
#
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
#
#
# if __name__ == '__main__':
#     link12 = ListNode(4)
#     link11 = ListNode(2, link12)
#     link31 = ListNode(-1)
#     link22 = ListNode(6)
#     link21 = ListNode(1, link22)
#     link41 = ListNode(9)
#     list = [link11, link21, link31, link41]
#     answer = Solution()
#     print(answer.mergeKLists(list))

def changeme(mylist):
    "修改传入的列表"
    mylist += 1
    print("函数内取值: ", mylist)
    return (mylist + 1)


# 调用changeme函数
mylist = 10
changeme(mylist)
print("函数外取值: ", mylist)