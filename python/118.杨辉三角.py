#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            # 1. 初始化当前行
            # 第 i 行有 i+1 个元素，先全部填 1
            # 比如 i=2 (第3行)，生成 [1, 1, 1]
            row = [1] * (i + 1)
            
            # 2. 计算中间的元素（除去首尾）
            # 只有当 i >= 2 时，这个循环才会执行
            # j 从 1 遍历到 i-1
            for j in range(1, i):
                # 状态转移方程：当前元素 = 上一行左上 + 上一行右上
                row[j] = ret[i-1][j-1] + ret[i-1][j]
            
            ret.append(row)
        return ret


# @lc code=end
numRows = 5
print(Solution().generate(numRows))
