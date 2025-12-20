#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 摩尔投票法 (Boyer-Moore Voting Algorithm)
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        
        
# @lc code=end

nums = [3,2,3]
print(Solution().majorityElement(nums))