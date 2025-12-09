#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        # 使用字典存储字符最后一次出现的索引
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 如果当前字符已经在窗口内出现过
            if s[right] in char_map and char_map[s[right]] >= left:
                # 将左边界直接跳到重复字符的下一位
                left = char_map[s[right]] + 1
            
            # 更新当前字符的位置
            char_map[s[right]] = right
            # 计算当前窗口长度并更新最大值
            max_len = max(max_len, right - left + 1)
            
        return max_len
        
        
        
# @lc code=end

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))