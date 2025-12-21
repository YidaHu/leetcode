#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 异或运算 (XOR) 的性质：
        # 1. a ^ 0 = a
        # 2. a ^ a = 0
        # 3. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        
        res = 0
        for num in nums:
            res ^= num
        return res
        
# @lc code=end

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))