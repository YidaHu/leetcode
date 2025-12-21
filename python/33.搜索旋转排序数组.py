#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # 核心思路：将数组一分为二，其中一定有一个半区是有序的
            
            # 1. 如果左半部分 [left, mid] 是有序的
            if nums[left] <= nums[mid]:
                # 检查 target 是否在这个有序区间内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左边找
                else:
                    left = mid + 1   # 去右边找
            
            # 2. 否则，右半部分 [mid, right] 肯定是有序的
            else:
                # 检查 target 是否在这个有序区间内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右边找
                else:
                    right = mid - 1  # 去左边找
                    
        return -1

        
# @lc code=end
nums = [5,1,3]
target = 5
print(Solution().search(nums, target))
