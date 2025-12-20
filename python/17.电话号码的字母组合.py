#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if not digits:
            return ret
        phone_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(index, path):
            if index == len(digits):
                ret.append(''.join(path))
                return
            digit = digits[index]
            letter = phone_map[digit]
            for l in letter:
                path.append(l)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return ret


# @lc code=end

digits = '23'
print(Solution().letterCombinations(digits))
