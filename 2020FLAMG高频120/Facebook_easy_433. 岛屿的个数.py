# Description
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
#
# Find the number of islands.
#
# Example
# Example 1:
#
# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3
#
# Example 2:
#
# Input:
# [
#   [1,1]
# ]
# Output:
# 1

# BFS
# 时间复杂度：O(n*m)
# n为行数，m为列数，显然，每个值为1的点都会被遍历一次
# 以下是lintcode的答案，input为boolean array，0和1本身可以代表True和False，例如grid[x][y]=0意思是False，可以直接if not grid[x][y], leetcode的input为string array,只能用if grid[x][y] == 0

from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    island += 1
        return island

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = dir_x + x
                next_y = dir_y + y
                if not self.isvalid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def isvalid(self, grid, x, y, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
            return grid[x][y]
        else:
            return False

# 以下是leetcode答案, input为string array
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    island += 1
        return island

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = dir_x + x
                next_y = dir_y + y
                if not self.isvalid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def isvalid(self, grid, x, y, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == '1':
            return True
        else:
            return False


# 并查集
# 时间复杂度：O(m Alpha(n))
# n次合并，m次查找的时间复杂度，这里Alpha是Ackerman函数的某个反函数，在很大的范围内这个函数的值可以看成是不大于4的，所以并查集的操作可以看作是线性的
# 以下是lintcode的答案，input为boolean array
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        self.island = 0
        self.pre = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.pre += [i * m + j]
                if grid[i][j]:
                    self.island += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < n and grid[i + 1][j] and grid[i][j]:
                    self.connect((i + 1) * m + j, i * m + j)
                if j + 1 < m and grid[i][j + 1] and grid[i][j]:
                    self.connect(i * m + j + 1, i * m + j)
        return self.island

    def connect(self, a, b):
        roota = self.unionfind(a)
        rootb = self.unionfind(b)
        if roota != rootb:
            self.pre[roota] = rootb
            self.island -= 1

    def unionfind(self, root):
        while root != self.pre[root]:
            root = self.pre[root]
        return root


# 以下是leetcode答案, input为string array
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        self.island = 0
        self.pre = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.pre += [i * m + j]
                if grid[i][j] == '1':
                    self.island += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < n and grid[i + 1][j] == '1' and grid[i][j] == '1':
                    self.connect((i + 1) * m + j, i * m + j)
                if j + 1 < m and grid[i][j + 1] == '1' and grid[i][j] == '1':
                    self.connect(i * m + j + 1, i * m + j)
        return self.island

    def connect(self, a, b):
        roota = self.unionfind(a)
        rootb = self.unionfind(b)
        if roota != rootb:
            self.pre[roota] = rootb
            self.island -= 1

    def unionfind(self, root):
        while root != self.pre[root]:
            root = self.pre[root]
        return root


# dfs
# 时间复杂度：O(n*m)
# n为行数，m为列数，显然，每个值为1的点都会被遍历一次
# 以下是lintcode的答案，input为boolean array
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    island += 1
        return island

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        n = len(grid)
        m = len(grid[0])
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_x = i + dir_x
            next_y = j + dir_y
            if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y]:
                self.dfs(grid, next_x, next_y)


# 以下是leetcode答案, input为string array
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island += 1
        return island

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        n = len(grid)
        m = len(grid[0])
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_x = i + dir_x
            next_y = j + dir_y
            if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == '1':
                self.dfs(grid, next_x, next_y)


if __name__ == '__main__':
    Grid = [[1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1]]
    answer = Solution()
    answers = answer.numIslands(Grid)
    print(answers)