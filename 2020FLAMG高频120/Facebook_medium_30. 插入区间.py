# Description
# Given a non-overlapping interval list which is sorted by start point.
#
# Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
# (2, 5) into [(1,2), (5,9)]
# Output:
# [(1,9)]
# Example 2:
#
# Input:
# (3, 4) into [(1,2), (5,9)]
# Output:
# [(1,2), (3,4), (5,9)]


# 时间复杂度O(n)
# n为数组的大小
# 空间复杂度O(n)
# n为数组的大小
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        newIntervals = []
        if len(intervals) == 0:
            newIntervals.append(newInterval)
        for i in range(len(intervals)):
            if newInterval.end < intervals[i].start:
                newIntervals.append(newInterval)
                for j in range(i, len(intervals)):
                    newIntervals.append(intervals[j])
                break
            elif newInterval.start > intervals[i].end:
                newIntervals.append(intervals[i])
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            if i == len(intervals) - 1:
                newIntervals.append(newInterval)
        return newIntervals

if __name__ == '__main__':
    input = [[1,3],[6,9]]
    insert = [2, 5]
    solution = Solution()
    answer = solution.insert(input, insert)
    print(answer)