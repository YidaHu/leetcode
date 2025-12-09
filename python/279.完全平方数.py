#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] 表示和为 i 的完全平方数的最少数量
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # 外层循环：遍历背包容量（从 1 到 n）
        for i in range(1, n + 1):
            # 内层循环：遍历物品（完全平方数 j*j）
            j = 1
            while j * j <= i:
                # 状态转移：当前解 vs (减去这个平方数后的最优解 + 1)
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]


# @lc code=end

n = 12
print(Solution().numSquares(n))
