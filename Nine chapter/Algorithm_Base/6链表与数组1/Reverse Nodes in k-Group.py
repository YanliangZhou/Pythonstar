# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
# For example, Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# 从头到尾打印链表
## 定义链表节点的类
class Node(object):
    # 节点有两个基础属性，1：该节点的值，2：下一个节点的地址
    def __init__(self, item):
        self.item = item
        self.next = None

    def travel(self):

        # 打印所有节点的值
        if self is None:
            return
        while self.next is not None:
            print(self.item, end=' ')
            self = self.next
        print(self.item)


# 定义链表的类
class SingleLinkList(object):
    def __init__(self):
        # 链表的基础属性：头结点
        self._head = None

    def append(self, item):
        # 在链表尾部增加一个节点
        node = Node(item)
        if self._head is None:
            self._head = node
            return
        cur_node = self._head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node

    def travel(self):
        # 打印链表
        if self._head is None:
            return
        cur_node = self._head
        while cur_node.next:
            print(cur_node.item, end=' ')
            cur_node = cur_node.next
        print(cur_node.item)

    def ReTravel(self):
        # 反转打印链表
        if self._head is None:
            return
        result = []  # this is a stack
        cur_node = self._head
        while cur_node.next is not None:
            result.insert(0, cur_node.item)
            cur_node = cur_node.next
        result.insert(0, cur_node.item)
        print(result)

    def ReConstruct(self):
        # 反转链表并打印
        if self._head is None:
            return
        L, M, R = None, None, self._head
        while R.next:
            L = M
            M = R
            R = R.next
            M.next = L
        R.next = M
        R.travel()


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print('顺序打印链表 ->> ', end='  ')
    ll.travel()
    print('反转打印链表 ->> ', end='  ')
    ll.ReTravel()
    print('反转链表并打印 ->> ', end='  ')
    ll.ReConstruct()