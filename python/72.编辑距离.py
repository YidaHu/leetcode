#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 使用递归 + 记忆化 (备忘录)
        # 这种写法更符合人类的直觉：遇到字符不一样，我就试这三种方法，看谁代价小
        
        memo = {}

        def dfs(i, j):
            # 查备忘录，如果算过直接返回
            if (i, j) in memo:
                return memo[(i, j)]
            
            # base case:
            # 如果 word1 走完了，剩下的 word2 只能全部插入
            if i == len(word1):
                return len(word2) - j
            # 如果 word2 走完了，剩下的 word1 只能全部删除
            if j == len(word2):
                return len(word1) - i
            
            # 核心逻辑
            if word1[i] == word2[j]:
                # 字符一样，啥都不用做，直接跳过
                res = dfs(i + 1, j + 1)
            else:
                # 字符不一样，尝试三种操作，选最小的
                res = min(
                    dfs(i + 1, j),    # 删除 word1[i]
                    dfs(i, j + 1),    # 插入 word2[j]
                    dfs(i + 1, j + 1) # 替换 word1[i] -> word2[j]
                ) + 1
            
            # 记入备忘录
            memo[(i, j)] = res
            return res

        return dfs(0, 0)
        
# @lc code=end

word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))