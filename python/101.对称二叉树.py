#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        queue = [root.left, root.right]  # 一开始就放左右两个

        while queue:
            # 每次取两个出来比较（像照镜子一样）
            left = queue.pop(0)
            right = queue.pop(0)

            # 1. 两个都为空：对称，继续下一对
            if not left and not right:
                continue

            # 2. 一个空一个不空，或者值不相等：不对称，直接死刑
            if not left or not right or left.val != right.val:
                return False

            # 3. 把孩子加入队列（注意顺序：外侧对外侧，内侧对内侧）
            # 左节点的左孩子 vs 右节点的右孩子
            queue.append(left.left)
            queue.append(right.right)

            # 左节点的右孩子 vs 右节点的左孩子
            queue.append(left.right)
            queue.append(right.left)

        return True


# @lc code=end

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(Solution().isSymmetric(root))  # 输出应为 True
