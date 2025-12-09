#!/usr/bin/env python
"""
@File    :   lc11.py
@Time    :   2025/12/03 15:58:10
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   11. 盛最多水的容器
"""

# 11. 盛最多水的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
#
# 示例 1：
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例 2：
# 输入：height = [1,1]
# 输出：1
#
# 提示：
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

from typing import List


class Solution:
    def maxArea(self, nums: List[int]) -> int:
        """
        计算盛最多水的容器的面积。
        
        思路：双指针法
        1. 初始化两个指针，left 指向数组开头，right 指向数组结尾。
        2. 容器的宽度为 right - left，高度为 min(nums[left], nums[right])。
        3. 计算当前面积，并更新最大面积。
        4. 移动指针：为了找到更大的面积，我们需要保留较高的一边，移动较短的一边。
           如果 nums[left] < nums[right]，则 left 右移；否则 right 左移。
           这是因为如果移动较高的一边，宽度减小，而高度不可能增加（受限于较短的一边），面积只会减小。
           只有移动较短的一边，才有可能找到更高的边，从而增加面积。
        
        时间复杂度：O(n)，其中 n 是数组的长度。双指针总共遍历一次数组。
        空间复杂度：O(1)，只需要常数空间。
        """
        length = len(nums)
        # 初始化双指针，i 指向头，j 指向尾
        i, j = 0, length - 1
        max_areas = 0
        
        while i < j:
            # 计算当前面积：高度取决于较短的一边，宽度为 j - i
            # 如果左边较低
            if nums[i] <= nums[j]:
                # 计算面积：左边高度 * 宽度
                current_area = nums[i] * (j - i)
                max_areas = max(max_areas, current_area)
                # 移动左指针，尝试寻找更高的左边界
                i += 1
            else:
                # 如果右边较低（或相等）
                # 计算面积：右边高度 * 宽度
                current_area = nums[j] * (j - i)
                max_areas = max(max_areas, current_area)
                # 移动右指针，尝试寻找更高的右边界
                j -= 1

        return max_areas


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(nums))
