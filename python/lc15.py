#!/usr/bin/env python
"""
@File    :   lc15.py
@Time    :   2025/12/03 16:55:53
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   15. 三数之和
"""

# 15. 三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
# 示例 2：
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
# 示例 3：
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
# 提示：
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        计算所有和为 0 且不重复的三元组。
        
        思路：排序 + 双指针
        1. 特判：如果数组为空或长度小于3，直接返回空列表。
        2. 排序：对数组进行从小到大排序，方便后续使用双指针和去重。
        3. 遍历：遍历数组，固定第一个数 nums[i]。
           - 如果 nums[i] > 0：因为数组已排序，后面的数都大于0，三数之和不可能为0，直接结束循环。
           - 去重：如果 nums[i] == nums[i-1]，说明该数字已经作为第一个数处理过，跳过以避免重复。
           - 双指针：令 left = i + 1, right = n - 1。
             - 当 left < right 时，计算 sum = nums[i] + nums[left] + nums[right]。
             - 如果 sum == 0：找到一个解，加入结果集。
               - 去重：跳过重复的 nums[left]。
               - 去重：跳过重复的 nums[right]。
               - 移动指针：left++, right--。
             - 如果 sum > 0：说明和太大，需要减小，right--。
             - 如果 sum < 0：说明和太小，需要增大，left++。
        
        时间复杂度：O(n^2)，其中 n 是数组长度。排序 O(nlogn)，双指针遍历 O(n^2)。
        空间复杂度：O(1) 或 O(logn)，取决于排序算法的空间消耗（忽略存储结果的空间）。
        """
        if not nums or len(nums) < 3:
            return []
        
        n = len(nums)
        nums.sort() # 排序
        res = []
        
        for i in range(n):
            # 如果当前数字大于0，则三数之和一定大于0，结束循环
            if nums[i] > 0:
                break # 这里应该是 break 而不是 return res，虽然在这个特定逻辑下 return res 也是对的，但 break 更符合语义
            
            # 去重：如果当前数字和前一个数字相同，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 双指针
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重：跳过相同的左边界
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重：跳过相同的右边界
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 找到答案后，双指针同时收缩
                    left += 1
                    right -= 1
                elif current_sum > 0:
                    # 和大于0，说明右边的数太大了，右指针左移
                    right -= 1
                else:
                    # 和小于0，说明左边的数太小了，左指针右移
                    left += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
