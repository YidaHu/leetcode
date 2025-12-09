#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        思路讲解（双指针法）：
        想象我们在向中间挤压。
        对于每一个位置，它能接多少雨水，取决于它左右两边最高的柱子中较矮的那根（木桶效应）。
        
        我们维护两个指针 left 和 right，以及两个变量 left_max 和 right_max。
        left_max: 从左边看过来，目前最高的柱子。
        right_max: 从右边看过来，目前最高的柱子。
        
        核心逻辑：
        如果 left_max < right_max：
            说明对于 left 指针当前的位置，左边的墙（left_max）比右边的墙（至少有 right_max 这么高）要矮。
            根据木桶效应，水位高度由矮的墙决定，也就是 left_max。
            所以我们可以确定 left 位置的水量，并移动 left。
        否则：
            说明右边的墙更矮（或者一样高），水位由 right_max 决定。
            我们可以确定 right 位置的水量，并移动 right。
        """
        n = len(height)
        # 如果数组为空，无法接雨水，直接返回0
        if n == 0:
            return 0
        
        water = 0
        # 初始化双指针，left指向数组开头，right指向数组结尾
        left, right = 0, n - 1
        # 初始化左右两边的最大高度，分别记录从左边和右边看到的最高柱子
        left_max, right_max = height[left], height[right]
        
        # 当两个指针没有相遇时，持续向中间移动
        while left < right:
            # 比较左右两边的最大高度
            # 如果左边的最大高度小于右边的最大高度，说明瓶颈在左边
            # 根据木桶效应，接水量取决于较短的一边，即 left_max
            if left_max < right_max:
                # 移动左指针
                left += 1
                # 更新左边的最大高度：如果当前柱子比之前的 left_max 高，则更新 left_max
                left_max = max(left_max, height[left])
                # 计算当前位置的接水量：
                # 因为 left_max < right_max，所以当前位置的水位高度由 left_max 决定
                # 水量 = 水位高度 (left_max) - 当前柱子高度 (height[left])
                # 注意：如果 height[left] 更新了 left_max，那么 left_max - height[left] 为 0，表示不积水
                water += left_max - height[left]
            else:
                # 如果右边的最大高度小于等于左边的最大高度，说明瓶颈在右边
                # 接水量取决于 right_max
                right -= 1
                # 更新右边的最大高度
                right_max = max(right_max, height[right])
                # 计算当前位置的接水量
                # 水量 = 水位高度 (right_max) - 当前柱子高度 (height[right])
                water += right_max - height[right]
                
        return water        


# @lc code=end

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
