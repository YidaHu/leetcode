#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0_flag = False
        col0_flag = False

        # 1. 检查第一行是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        
        # 2. 检查第一列是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 3. 使用第一行和第一列作为标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 4. 根据标记置零内部元素
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 5. 处理第一行
        if row0_flag:
            for j in range(n):
                matrix[0][j] = 0
        
        # 6. 处理第一列
        if col0_flag:
            for i in range(m):
                matrix[i][0] = 0
        
        
# @lc code=end

matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Solution().setZeroes(matrix)
print(matrix)