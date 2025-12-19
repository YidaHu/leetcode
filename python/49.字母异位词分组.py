#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        # 使用字典存储分组结果，键为排序后的字符串，值为对应的异位词列表
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 对字符串进行排序，得到标准形式
            sorted_str = ''.join(sorted(s))
            # 将原字符串添加到对应的异位词组中
            anagram_map[sorted_str].append(s)
        
        # 返回所有的异位词组
        return list(anagram_map.values())
        
# @lc code=end

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))