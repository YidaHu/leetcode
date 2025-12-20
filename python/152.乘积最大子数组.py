#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        # 维护当前位置的最大乘积和最小乘积
        # 因为负数乘以负数会变正数，所以最小值可能翻身变最大值
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            # 如果当前是负数，最大值和最小值会互换
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod
            
            # 状态转移：要么是当前数自己（重新开始），要么是累乘之前的
            max_prod = max(curr, max_prod * curr)
            min_prod = min(curr, min_prod * curr)
            
            res = max(res, max_prod)
            
        return res
        
# @lc code=end

nums = [-2,3,-4]
print(Solution().maxProduct(nums))