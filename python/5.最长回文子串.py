#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        
        for i in range(len(s)):
            # 1. 奇数长度尝试：以 s[i] 为中心
            len1 = self.expandAroundCenter(s, i, i)
            # 2. 偶数长度尝试：以 s[i] 和 s[i+1] 为中心
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 3. 谁长听谁的
            max_len = max(len1, len2)
            
            # 4. 如果发现了更长的，更新全局答案的坐标
            if max_len > end - start:
                # 这一步是根据中心点 i 和长度 max_len 倒推起点和终点
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
    
    # 辅助函数：给定中心，向两边扩散
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 此时 left 和 right 已经多走了一步（不满足条件了）
        # 实际长度公式推导：(right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
        
# @lc code=end
s = "babad"
print(Solution().longestPalindrome(s))
