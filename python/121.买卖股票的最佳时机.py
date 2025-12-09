#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        # 1. 记录历史最低价 (初始化为无穷大，方便被第一个数更新)
        min_price = float('inf')
        
        # 2. 记录最大利润
        max_profit = 0
        
        for price in prices:
            # 情况一：发现更便宜的价格 -> 更新最低价
            # 此时我们不做交易，只是把"买入点"标记在今天
            if price < min_price:
                min_price = price
                
            # 情况二：今天的价格比最低价高 -> 尝试卖出
            # 算算利润：今天价格 - 历史最低价
            # 如果比之前的 max_profit 高，就更新答案
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        
# @lc code=end
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))
