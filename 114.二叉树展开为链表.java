/*
 * @lc app=leetcode.cn id=114 lang=java
 *
 * [114] 二叉树展开为链表
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

    /**
     * 将二叉树变链表
     * 
     * @param root
     */
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        // 将根节点的左子树变链表
        flatten(root.left);
        // 将根节点的右子树变链表
        flatten(root.right);
        TreeNode temp = root.right;
        // 把左边的树放到右边
        root.right = root.left;
        // 把左边置为空
        root.left = null;
        // 找到最右边节点
        while (root.right != null) {
            root = root.right;
        }
        // 把之前右边的，连接到新链表最右边
        root.right = temp;
    }
}
// @lc code=end
