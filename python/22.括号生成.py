#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        # left: 左括号已经用了几个
        # right: 右括号已经用了几个
        # path: 当前生成的字符串
        def backtrack(left, right, path):
            # 结束条件：左右括号都用完了 (一共 2n 个)
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # 剪枝条件1：左括号只要没用完，随时可以加
            if left < n:
                backtrack(left + 1, right, path + "(")
                
            # 剪枝条件2：右括号必须比左括号少的时候才能加
            # (也就是前面必须有未匹配的左括号，才能加右括号)
            if right < left:
                backtrack(left, right + 1, path + ")")
                
        backtrack(0, 0, "")
        return res
        
# @lc code=end
n = 3
print(Solution().generateParenthesis(n))
