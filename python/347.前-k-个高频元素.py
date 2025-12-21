#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. 统计频率: O(N)
        # map: {num: count}
        count_map = Counter(nums)
        
        # 2. 使用小顶堆维护前 k 个高频元素: O(N log k)
        # 堆里的元素是元组 (freq, num)，Python 会默认按第一个元素(freq)进行比较
        min_heap = []
        
        for num, freq in count_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                # 如果当前频率比堆顶（堆里最小的频率）大，就替换掉堆顶
                if freq > min_heap[0][0]:
                    heapq.heapreplace(min_heap, (freq, num))
        
        # 3. 取出堆中的数字
        # 此时堆里存的是频率最高的 k 个，虽然是小顶堆，但我们要的是这些数字本身
        return [item[1] for item in min_heap]

# 也可以直接用一行代码 (面试时最好手写上面的堆逻辑)
# return [item[0] for item in Counter(nums).most_common(k)]
# @lc code=end

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
