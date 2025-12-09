#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        # answer[i] 将用来存储索引 i 左侧所有元素的乘积
        answer = [0] * length
        
        # 1. 先从左往右遍历，计算"左积"
        # answer[0] 左边没有元素，所以是 1
        answer[0] = 1
        for i in range(1, length):
            # 当前位置的左积 = 前一个位置的左积 * 前一个位置的数
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # 2. 再从右往左遍历，计算"右积"，并直接乘入结果
        # R 用来动态维护右边所有元素的乘积
        R = 1
        for i in reversed(range(length)):
            # 最终结果 = 左积 * 右积
            answer[i] = answer[i] * R
            # 更新右积，把当前数乘进去
            R *= nums[i]
        
        return answer


# @lc code=end

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))