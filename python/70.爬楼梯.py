#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. 特殊情况：如果只有 1 阶或 2 阶，直接返回 n
        if n <= 2:
            return n
        
        # 2. 滚动数组优化
        # 我们不需要开一个大数组 dp[] 来存所有的值，因为我们只需要前两个数
        a = 1  # 代表 f(i-2)
        b = 2  # 代表 f(i-1)
        
        # 从第 3 阶开始算
        for i in range(3, n + 1):
            current = a + b  # f(i) = f(i-2) + f(i-1)
            
            # 往前滚动
            a = b
            b = current
            
        return b
        
        
# @lc code=end

n = 3
print(Solution().climbStairs(n))