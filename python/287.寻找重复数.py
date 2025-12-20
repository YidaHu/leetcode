#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针法 (Floyd's Tortoise and Hare)
        # 将数组视为链表：i -> nums[i]
        # 因为有重复数字，所以一定存在环，且环的入口就是重复的数字
        
        # 1. 寻找相遇点
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # 2. 寻找环入口
        # 当快慢指针相遇时，让 slow 回到起点
        # 然后两个指针每次都走一步，再次相遇的地方就是环入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
# @lc code=end

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))