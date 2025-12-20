#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return False
        max_v = 0
        count = 0
        for num in nums:
            max_v = max(max_v, num)
            count += num
        if count % 2 != 0:
            return False
        avg = int(count / 2)
        if max_v > avg:
            return False

        dp = [False] * (avg + 1)
        dp[0] = True
        for num in nums:
            # 修正：起点应该是 avg (目标值)，而不是 max_v
            for j in range(avg, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                
        if dp[avg]:
            return True
        return False


# @lc code=end
nums = [2, 2, 3, 5]
print(Solution().canPartition(nums))
