#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        
        思路：广度优先搜索 (BFS)
        层序遍历就是一层一层地从左到右访问节点。
        最适合的数据结构是【队列】(Queue)，因为队列是先进先出 (FIFO) 的。
        
        算法步骤：
        1. 初始化：如果根节点为空，直接返回空列表。否则，将根节点放入队列。
        2. 循环：只要队列不为空，就一直循环处理。
        3. 处理每一层：
           - 记录当前队列的长度 (size)，这个 size 就是当前这一层的节点个数。
           - 遍历 size 次，依次取出队首节点。
           - 将取出的节点值加入当前层的列表 (current_level)。
           - 如果该节点有左孩子，将左孩子加入队列。
           - 如果该节点有右孩子，将右孩子加入队列。
        4. 收集结果：每处理完一层，将 current_level 加入最终结果 result。
        """
        # 1. 边界条件处理：如果树为空，直接返回空列表
        if not root:
            return []
        
        # 2. 初始化队列，先把根节点放进去
        # 队列用于存储等待被处理的节点
        queue = [root]
        result = []
        
        # 3. 开始循环，直到队列为空（说明所有节点都处理完了）
        while queue:
            # 记录当前层的节点数量
            # 这一步非常关键！它锁定了当前层有多少个节点需要处理。
            # 在这个 for 循环执行过程中新加入队列的节点（孩子节点），属于下一层，不会在本次循环中被处理。
            size = len(queue)
            current_level = []
            
            # 4. 遍历当前层的每一个节点
            for _ in range(size):
                # 取出队首节点 (pop(0) 操作)
                node = queue.pop(0)
                # 将节点值加入当前层的结果列表
                current_level.append(node.val)
                
                # 5. 将当前节点的孩子节点加入队列（为下一层做准备）
                # 如果有左孩子，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果有右孩子，加入队列
                if node.right:
                    queue.append(node.right)
            
            # 6. 将这一层的结果加入总结果列表
            result.append(current_level)
            
        return result


# @lc code=end

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
