#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
            
        # left[i] 代表 i 左边第一个比它矮的下标
        # 初始化为 -1 (代表左边没有比它矮的了，边界在最左侧之外)
        left = [-1] * n
        
        # right[i] 代表 i 右边第一个比它矮的下标
        # 初始化为 n (代表右边没有比它矮的了，边界在最右侧之外)
        right = [n] * n
        
        # 1. 计算左边界
        for i in range(n):
            p = i - 1
            # 核心优化：如果前一个柱子比当前高，就直接跳到前一个柱子的左边界去
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
            
        # 2. 计算右边界 (注意要从右往左遍历)
        for i in range(n - 1, -1, -1):
            p = i + 1
            # 核心优化：如果后一个柱子比当前高，就直接跳到后一个柱子的右边界去
            while p < n and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
            
        # 3. 计算最大面积
        max_area = 0
        for i in range(n):
            # 宽度 = 右边界 - 左边界 - 1
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area
        
# @lc code=end

heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))