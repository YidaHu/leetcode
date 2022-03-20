import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=1373 lang=java
 *
 * [1373] 二叉搜索子树的最大键值和
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

    int sum = 0;

    public int maxSumBST(TreeNode root) {
        traverse(root);
        return sum;
    }

    public int[] traverse(TreeNode root) {
        if (root == null) {
            return new int[]{1, Integer.MAX_VALUE, Integer.MIN_VALUE, 0};
        }
        // 左子树
        int[] left = traverse(root.left);
        // 右子树
        int[] right = traverse(root.right);
        // 后序遍历位置
        int[] res = new int[4];
        // 是BFS的条件如下：
        // 1、左右子树均为BFS；
        // 2、根节点值大于左子树的最大值；
        // 3、根节点值小于右子树的最小值。
        if (left[0] == 1 && right[0] == 1
            && root.val > left[2] && root.val < right[1]) {
            // 记录符合BST
            res[0] = 1;
            // 最小值
            res[1] = Math.min(left[1], root.val);
            // 最大值
            res[2] = Math.max(right[2], root.val);
            // 节点键值和
            res[3] = left[3] + right[3] + root.val;
            // 记录最大值
            sum = Math.max(sum, res[3]);
        } else {
            res[0] = 0;
        }
        return res;
    }

}
// @lc code=end

