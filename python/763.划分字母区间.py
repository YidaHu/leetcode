#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i

        res = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_index[char])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res


# @lc code=end

s = 'ababcbacadefegdehijhklij'
print(Solution().partitionLabels(s))
