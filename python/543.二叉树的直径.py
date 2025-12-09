#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 记录全局最大直径
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return 0
            
            # 1. 问左孩子：你有多高？
            left_height = get_height(node.left)
            
            # 2. 问右孩子：你有多高？
            right_height = get_height(node.right)
            
            # 3. 搞事情：如果以我为"拐点"，路径长度是多少？
            # 直径 = 左臂长 + 右臂长
            # 我们在遍历每个节点时，都去更新一下全局最大值
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # 4. 向上汇报：告诉我的父节点我有多高
            # 我的高度 = 最高的那个孩子 + 我自己(1)
            return max(left_height, right_height) + 1
            
        get_height(root)
        return self.max_diameter
# @lc code=end

