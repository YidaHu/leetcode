#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1. 从后向前查找第一个相邻升序对 (i, i+1)，满足 nums[i] < nums[i+1]
        # 此时 [i+1, end] 必然是降序的
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 2. 如果找到了这样的 i
        if i >= 0:
            # 从后向前查找第一个大于 nums[i] 的数 nums[j]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. 反转 [i+1, end] 区间，使其变为升序
        # 如果步骤 1 没找到 i (即 i = -1)，说明整个数组是降序的，直接反转整个数组即可
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
# @lc code=end
nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)
