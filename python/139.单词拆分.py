#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        思路讲解（动态规划）：
        
        我们要判断字符串 s 是否可以被拆分成字典中的单词。
        这个问题可以分解为子问题：
        如果 s[0...i] 可以被拆分，那么可能存在一个分割点 j (0 <= j < i)，
        使得 s[0...j] 可以被拆分（即 dp[j] 为 True），并且 s[j...i] 是字典中的一个单词。
        
        定义状态：
        dp[i] 表示字符串 s 的前 i 个字符（即 s[0...i-1]）是否可以被拆分成字典中的单词。
        
        状态转移方程：
        dp[i] = True，如果存在一个 j (0 <= j < i)，满足 dp[j] == True 且 s[j:i] 在 wordDict 中。
        
        初始化：
        dp[0] = True。表示空字符串可以被拆分（这是一个基础条件，为了让后续计算能进行下去）。
        dp 数组长度为 len(s) + 1，其余初始化为 False。
        
        遍历顺序：
        i 从 1 到 n (包含 n)。
        j 从 0 到 i-1。
        """
        n = len(s)
        # 为了快速查找，将列表转换为哈希集合
        word_set = set(wordDict)
        
        # dp[i] 表示 s 的前 i 个字符是否能被拆分
        dp = [False] * (n + 1)
        dp[0] = True
        
        # 遍历背包（字符串长度）
        for i in range(1, n + 1):
            # 遍历物品（分割点）
            for j in range(i):
                # 如果前 j 个字符可以拆分，且从 j 到 i 的子串也在字典中
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # 只要找到一种拆分方式即可，不需要继续找了
        
        return dp[n]

# @lc code=end

s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
