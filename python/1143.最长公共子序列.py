#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        
        # dp[i][j] 表示 text1[0...i-1] 和 text2[0...j-1] 的最长公共子序列长度
        # 多一行一列是为了处理空字符串的情况，方便边界处理
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前字符相等，则长度 = 左上角 + 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 如果不相等，则继承左边或者上边的最大值
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
        
# @lc code=end

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))