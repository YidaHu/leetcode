#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        优化思路：滑动窗口 + 数组计数
        时间复杂度：O(N)，其中 N 是字符串 s 的长度。
        空间复杂度：O(1)，因为只需要大小为 26 的数组。
        """
        s_len, p_len = len(s), len(p)

        # 如果 s 比 p 短，不可能包含 p 的异位词
        if s_len < p_len:
            return []

        # 初始化计数数组 (26个字母)
        # p_count: 记录 p 中字符的频率
        # s_count: 记录当前窗口中字符的频率
        p_count = [0] * 26
        s_count = [0] * 26

        # 1. 先统计 p 的字符，以及 s 中第一个窗口的字符
        for i in range(p_len):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        ret = []

        # 2. 检查第一个窗口是否匹配
        if s_count == p_count:
            ret.append(0)

        # 3. 开始滑动窗口
        # i 是当前窗口最左侧的索引，即将被移出的那个字符的索引
        for i in range(s_len - p_len):
            # 窗口右移操作：
            # 1. 移除左边的字符 s[i]
            s_count[ord(s[i]) - ord('a')] -= 1
            # 2. 加入右边的字符 s[i + p_len]
            s_count[ord(s[i + p_len]) - ord('a')] += 1

            # 3. 比较计数数组
            # 这里的 i+1 是因为当前窗口的起始位置已经向右移动了一格
            if s_count == p_count:
                ret.append(i + 1)

        return ret


# @lc code=end

s = 'cbaebabacd'
p = 'abc'
print(Solution().findAnagrams(s, p))
