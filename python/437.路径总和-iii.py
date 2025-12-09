#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # key: 前缀和, value: 该前缀和出现的次数
        # 初始化 {0: 1} 是为了处理"从根节点开始就满足条件"的情况
        # 比如 target=8, 路径是 8, 此时 curr=8, curr-target=0, 需要 map[0] = 1
        self.prefix_map = {0: 1}
        self.count = 0
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            # 1. 更新当前路径的前缀和
            curr_sum += node.val
            
            # 2. 核心逻辑：两数之和的变种
            # 如果 (curr_sum - target) 存在于 map 中
            # 说明中间有一段路径的和刚好等于 target
            # 比如：root->...->A->...->B (当前)
            # prefix(B) - prefix(A) = target  =>  prefix(A) = prefix(B) - target
            self.count += self.prefix_map.get(curr_sum - targetSum, 0)
            
            # 3. 将当前前缀和加入 map，准备处理子节点
            self.prefix_map[curr_sum] = self.prefix_map.get(curr_sum, 0) + 1
            
            # 4. 继续递归
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # 5. 回溯（非常重要！）
            # 当我们离开这个节点返回父节点时，这个节点的前缀和就不应该被其他路径（比如兄弟节点）用到了
            # 所以要把它从 map 中移除（次数减 1）
            self.prefix_map[curr_sum] -= 1
            
        dfs(root, 0)
        return self.count
# @lc code=end

