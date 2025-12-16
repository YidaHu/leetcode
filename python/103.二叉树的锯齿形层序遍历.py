#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        import collections
        queue = collections.deque([root])
        res = []
        is_order_left = True # True: 从左往右, False: 从右往左
        
        while queue:
            level_size = len(queue)
            level_vals = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 如果是从右往左，就把这一层的结果翻转一下
            if not is_order_left:
                level_vals.reverse()
            
            res.append(level_vals)
            # 切换方向
            is_order_left = not is_order_left
            
        return res
        
# @lc code=end

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))