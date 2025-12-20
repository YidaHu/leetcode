#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        if nums[0] >= target:
            return 0
        if n == 1 and nums[0] < target:
            return 1

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[right] < target:
                return right + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left


# @lc code=end

nums = [1]
target = 2
print(Solution().searchInsert(nums, target))
