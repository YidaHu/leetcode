/*
 * @lc app=leetcode.cn id=226 lang=java
 *
 * [226] 翻转二叉树
 */

// @lc code=start

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        // 前序节点位置
        // 左右节点交换位置
        TreeNode tempNode = root.left;
        root.left = root.right;
        root.right = tempNode;
        // 让左右子树继续翻转
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
// @lc code=end
