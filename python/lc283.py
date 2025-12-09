# 283 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 示例 2:
# 输入: nums = [0]
# 输出: [0]
#
# 提示:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
# 进阶：你能尽量减少完成的操作次数吗？

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        思路：双指针
        时间复杂度：O(n)，其中 n 是数组的长度。每个元素最多被访问两次。
        空间复杂度：O(1)，只需要常数空间存放指针变量。
        """
        # 如果数组长度为1，直接返回，不需要处理
        if len(nums) == 1:
            return nums
        
        n = len(nums)
        # 使用双指针法
        # left 指针指向当前已经处理好的非零序列的尾部（即下一个非零元素应该放置的位置）
        # right 指针用于遍历数组
        left = right = 0
        
        while right < n:
            # 如果当前元素 nums[right] 不为 0
            if nums[right] != 0:
                # 将非零元素交换到 left 指向的位置
                # 这样可以保证 left 左边的所有元素都是非零的（或者在处理过程中保持相对顺序）
                nums[left], nums[right] = nums[right], nums[left]
                # left 指针向右移动，准备放置下一个非零元素
                left += 1
            # right 指针始终向右移动，继续检查下一个元素
            right += 1

        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
