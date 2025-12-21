#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def rightSideView(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root or root.val is None:
            return []
        res = []
        queue = deque([root])

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if i == n - 1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res


# @lc code=end
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(0)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
print(Solution().rightSideView(root))
