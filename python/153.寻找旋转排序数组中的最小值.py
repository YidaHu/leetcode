#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 核心逻辑：拿中间值和最右边比
            if nums[mid] > nums[right]:
                # 中间值 > 右边值，说明 mid 在左半边的“高坡”上
                # 最小值肯定在 mid 的右边
                left = mid + 1
            else:
                # 中间值 <= 右边值，说明 mid 在右半边的“低坡”上
                # 最小值可能是 mid 自己，或者在 mid 左边
                right = mid
                
        return nums[left]
        
# @lc code=end

nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))