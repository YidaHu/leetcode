#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def bt(index, path):
            res.append(path[:])

            for i in range(index, n):
                path.append(nums[i])

                bt(i + 1, path)

                path.pop()

        bt(0, [])

        return res


# @lc code=end

nums = [1, 2, 3]
print(Solution().subsets(nums))
