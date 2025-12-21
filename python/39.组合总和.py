#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def bt(start_index, path, current_sum):
            if current_sum == target:
                res.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                if current_sum + candidates[start_index] > target:
                    break

                path.append(candidates[i])

                bt(i, path, current_sum + candidates[i])

                path.pop()

        bt(0, [], 0)
        return res


# @lc code=end
candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
