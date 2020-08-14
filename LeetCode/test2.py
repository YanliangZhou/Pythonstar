class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

node1 = Treenode(3)
node2 = Treenode(1)
node3 = Treenode(4)
node4 = Treenode(6)
node5 = Treenode(7)

node1.left = node2
node1.right = node4

node4.left = node3
node4.right = node5

class Solution:
    def findpath(self,root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        treepath = [str(root.val)+'->'+path for path in self.findpath(root.left)]
        treepath += [str(root.val)+'->'+path for path in self.findpath(root.right)]
        return treepath

if __name__ == '__main__':
    Path = Solution()
    print(Path.findpath(node1))