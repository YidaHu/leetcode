#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 1. 初始化 dp 数组
        # 长度为 amount + 1，因为要存 0 到 amount 的所有状态
        # 初始值设为 amount + 1，这是一个不可能达到的最大值（相当于无穷大），方便后面取 min
        dp = [amount + 1] * (amount + 1)
        
        # 2. 基础状态
        dp[0] = 0  # 凑 0 元需要 0 个硬币
        
        # 3. 外层循环：遍历所有金额，从 1 算到 amount
        for i in range(1, amount + 1):
            # 4. 内层循环：尝试每一种硬币
            for coin in coins:
                # 如果当前金额 i 够减去这枚硬币
                if i >= coin:
                    # 核心公式：
                    # dp[i] = min(当前记录的最小值, 用了这枚硬币后的数量)
                    # dp[i - coin] 是“减去这枚硬币后剩下的钱”所需的最少硬币数
                    # + 1 是加上当前这枚硬币
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 5. 返回结果
        # 如果 dp[amount] 还是初始值，说明怎么都凑不出来，返回 -1
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

# 测试
coins = [2, 5]
amount = 21
print(Solution().coinChange(coins, amount))
# @lc code=end