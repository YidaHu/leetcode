#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []

        def isPalindrome(substring):
            return substring == substring[::-1]

        def back(start_index, path):
            if start_index == len(s):
                res.append(path[:])
                return

            for i in range(start_index, len(s)):
                substring = s[start_index : i + 1]

                if isPalindrome(substring):
                    path.append(substring)
                    back(i + 1, path)
                    path.pop()

        back(0, path)
        return res


# @lc code=end
s = 'aab'
print(Solution().partition(s))
