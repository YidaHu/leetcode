#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = 0, len(matrix[0]) - 1
        while m < len(matrix) and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False


# @lc code=end

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 4
print(Solution().searchMatrix(matrix, target))
