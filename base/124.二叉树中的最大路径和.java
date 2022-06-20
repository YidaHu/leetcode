import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=124 lang=java
 *
 * [124] 二叉树中的最大路径和
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

    Integer maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return maxSum;
    }

    public int maxGain(TreeNode root) {
        if (root == null) {
            return 0;
        }
        // 递归左右节点
        // 只有最大贡献超过0，才会选择该节点
        int left = Math.max(maxGain(root.left), 0);
        int right = Math.max(maxGain(root.right), 0);
        // 最大路径和，取决于根和左右节点的和
        int priceNewPath = root.val + left +right;
        // 更新最大值
        maxSum = Math.max(maxSum, priceNewPath);
        // 返回节点最大贡献
        return root.val + Math.max(left, right);
    }
}
// @lc code=end

