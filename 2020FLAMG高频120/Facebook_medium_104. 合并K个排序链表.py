# Description
# Merge k sorted linked lists and return it as one sorted list.
#
# Analyze and describe its complexity.
#
# Have you met this question in a real interview?
# Example
# Example 1:
# 	Input:   [2->4->null,null,-1->null]
# 	Output:  -1->2->4->null
#
# Example 2:
# 	Input: [2->6->null,5->null,7->null]
# 	Output:  2->5->6->7->null


# 自底向上的两两归并方法，最容易实现和思考
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        while len(lists) > 1:
            newlists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    newlist = self.merge_two_list(lists[i], lists[i + 1])
                    newlists.append(newlist)
                else:
                    newlists.append(lists[i])
            lists = newlists
        return lists[0]

    def merge_two_list(self, list1, list2):
        dummy = tail = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next


# 自顶向下的归并的方法。 归并排序写熟练的话，这个方法是最容易实现的。
# 易错：merge_two_list中循环退出判定条件原来用的是len（list），但下面只改变了start和end，list本身还没来得及变就进行下一轮递归，导致len(list)一直没变，导致stack over flow
# 因此，递归时需要注意退出的点有没有在被再次调用之前重新赋值
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        return self.merge_list(lists, 0, len(lists) - 1)

    def merge_list(self, list, start, end):
        while start < end:
            mid = start + (end - start) // 2
            left = self.merge_list(list, start, mid)
            right = self.merge_list(list, mid + 1, end)
            return self.merge_two_list(left, right)
        return list[start]

    def merge_two_list(self, list1, list2):
        dummy = tail = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next