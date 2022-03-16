import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=654 lang=java
 *
 * [654] 最大二叉树
 */

// @lc code=start

// Definition for a binary tree node.
// class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;

//     TreeNode() {
//     }

//     TreeNode(int val) {
//         this.val = val;
//     }

//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

class Solution {
    /**
     * 构建最大二叉树
     * 
     * @param nums
     * @return
     */
    public TreeNode constructMaximumBinaryTree(int[] nums) {

        TreeNode root = build(nums, 0, nums.length - 1);
        return root;
    }

    /**
     * 构建二叉树辅助函数
     * 
     * @param nums
     * @param left
     * @param right
     * @return
     */
    public TreeNode build(int[] nums, int left, int right) {
        if (nums.length == 0) {
            return null;
        }
        if (left > right) {
            return null;
        }
        int maxVal = Integer.MIN_VALUE;
        int index = -1;
        // 遍历获取区间内最大值及索引
        for (int i = left; i <= right; i++) {
            if (maxVal < nums[i]) {
                maxVal = nums[i];
                index = i;
            }
        }
        // 根节点填充最大值
        TreeNode root = new TreeNode(maxVal);
        // 左子树
        root.left = build(nums, left, index - 1);
        // 右子树
        root.right = build(nums, index + 1, right);
        return root;
    }
}
// @lc code=end
