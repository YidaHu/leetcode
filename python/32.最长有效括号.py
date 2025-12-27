#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left_count = 0
        right_count = 0
        for char in s:
            if char == '(':
                left_count += 1
            else:
                right_count += 1
            
            if left_count == right_count:
                max_len = max(max_len, left_count + right_count)
            elif right_count > left_count:
                left_count = 0
                right_count = 0

        left_count = 0
        right_count = 0
        for char in reversed(s):
            if char == '(':
                left_count += 1
            else:
                right_count += 1
            
            if left_count == right_count:
                max_len = max(max_len, left_count + right_count)
            elif left_count > right_count:
                left_count = 0
                right_count = 0
        
        return max_len
        
        
        
        
        
# @lc code=end

s = "(()"
print(Solution().longestValidParentheses(s))