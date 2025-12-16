#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        head = []
        
        for num in nums:
            heapq.heappush(head, num)
            
            if len(head) > k:
                heapq.heappop(head)
        
        return head[0]
        
# @lc code=end
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
