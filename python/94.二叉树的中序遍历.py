#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 结果数组
        res = []
        
        # 定义递归函数
        def dfs(node):
            if not node:
                return
            
            # 1. 先遍历左子树 (Left)
            dfs(node.left)
            
            # 2. 再处理当前节点 (Root)
            res.append(node.val)
            
            # 3. 最后遍历右子树 (Right)
            dfs(node.right)
            
        # 开始递归
        dfs(root)
        return res
        
# @lc code=end
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().inorderTraversal(root))
