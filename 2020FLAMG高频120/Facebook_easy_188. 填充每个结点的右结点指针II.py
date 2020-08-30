# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#     Example 1:
#
#     Input: root = [1, 2, 3, 4, 5, null, 7]
#     Output: [1,  # ,2,3,#,4,5,7,#]
#     Explanation: Given the above binary tree(Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
# Constraints:
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 使用额外队列来完成异父子节点之间的链接
# 复杂度分析
# 时间复杂度：O(N)O(N)，每个节点被访问一次，即从队列中弹出，并建立 next 指针。
# 空间复杂度：O(N)O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2N/2 个节点。广度优先遍历的复杂度取决于一个层级上的最大元素数量。这种情况下空间复杂度为 O(N)O(N)。

import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                cur = Q.popleft()
                if i < size - 1:
                    cur.next = Q[0]
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
        return root


# 判定左右子节点是否有pre节点，并用next来完成左右异父子节点间的链接
# 复杂度分析
# 时间复杂度：O(N)O(N)，每个节点只处理一次。
# 空间复杂度：O(1)O(1)，不使用额外空间。

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            pre = head = None
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                        pre = pre.next
                    else:
                        pre = head = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                        pre = pre.next
                    else:
                        pre = head = cur.right
                cur = cur.next
        return root
