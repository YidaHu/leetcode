/*
 * @lc app=leetcode.cn id=700 lang=java
 *
 * [700] 二叉搜索树中的搜索
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    TreeNode node = null;

    public TreeNode searchBST(TreeNode root, int val) {
        traverse(root, val);
        return node;
    }

    public void traverse(TreeNode root, int val) {
        if (root == null) {
            return;
        }
        if (root.val == val) {
            node = root;
            return;
        }
        if (root.val < val) {
            traverse(root.right, val);
        }
        if (root.val > val) {
            traverse(root.left, val);
        }
    }

}
// @lc code=end

