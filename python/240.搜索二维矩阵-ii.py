#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
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

        m, n = len(matrix), len(matrix[0])

        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


# @lc code=end

matrix = [[-5]]
target = -5
print(Solution().searchMatrix(matrix, target))
