/*
 * @lc app=leetcode.cn id=701 lang=java
 *
 * [701] 二叉搜索树中的插入操作
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

    public TreeNode insertIntoBST(TreeNode root, int val) {
        // 化身为节点
        TreeNode node = new TreeNode(val);
        // 节点为null，直接插
        if (root == null) {
            return node;
        }
        // 左右节点为空，根据大小插一下
        if (root.left == null && root.right == null) {
            if (root.val > val) {
                root.left = node;
                return root;
            } 
            if (root.val < val) {
                root.right = node;
                return root;
            } 

        }
        // 进左子树处理
        if (root.val > val ) {
            if (root.left == null) {
                root.left = node;
            } else {
                root.left = insertIntoBST(root.left, val);
            }
        }
        // 进右子树
        if (root.val < val ) {
            if (root.right == null) {
                root.right = node;
            } else {
                root.right = insertIntoBST(root.right, val);
            }
        }
        return root;

    }


}
// @lc code=end

