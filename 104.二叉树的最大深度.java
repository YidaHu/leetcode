import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=104 lang=java
 *
 * [104] 二叉树的最大深度
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
    HashMap<Integer, Integer> map = new HashMap();
    int flag = 0;
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        traverse(root, 0);
        int max = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (max < entry.getValue()) {
                max = entry.getValue();
            }
        }
        return max;
    }
    
    public void traverse(TreeNode root, int record) {
        flag = flag + 1;
        if (root == null) {
            return;
        }
        record += 1;
        map.put(flag, record);
        traverse(root.left, record);
        traverse(root.right, record);
    }
}
// @lc code=end

