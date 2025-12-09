#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key: 数字, value: 索引
        mp = {}
        
        for i, num in enumerate(nums):
            # 1. 算出我想找的"另一半"
            complement = target - num
            
            # 2. 回头看：之前的数字里有没有"另一半"？
            if complement in mp:
                # 找到了！直接返回 [另一半的索引, 当前索引]
                return [mp[complement], i]
            
            # 3. 没找到：把自己存进通讯录，等待有缘人（后面的数字）来找我
            mp[num] = i
            
        return []


# @lc code=end

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
