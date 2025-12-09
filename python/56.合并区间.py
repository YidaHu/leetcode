#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. 关键步骤：按照左端点排序
        # 这样我们只需要关注"当前区间"和"结果集中最后一个区间"的关系
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # 情况一：没有重叠
            # 如果结果集为空，或者 当前区间的左边 > 上一个区间的右边
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 情况二：发生重叠
                # 不需要添加新元素，而是修改上一个元素的右边界
                # 谁结束得晚，就听谁的
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


# @lc code=end
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
