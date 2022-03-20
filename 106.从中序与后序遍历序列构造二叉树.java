/*
 * @lc app=leetcode.cn id=106 lang=java
 *
 * [106] 从中序与后序遍历序列构造二叉树
 */

// @lc code=start

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return build(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
    }

    public TreeNode build(int[] inorder, int inStart, int inEnd,
                        int[] postorder, int postStart, int postEnd) {
        // base case
        if (inStart > inEnd) {
            return null;
        }
        // 后序遍历最后一个节点为根节点
        int rootVal = postorder[postEnd];
        int index = -1;
        // 遍历查找根节点在中序遍历中的下标
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == rootVal) {
                index = i;
                break;
            }
        }
        // 计算左子树的范围
        int leftSize = index - inStart;
        // 构建根节点
        TreeNode root = new TreeNode(rootVal);
        // 构建左子树
        root.left = build(inorder, inStart, index - 1, postorder, postStart, postStart + leftSize - 1);
        // 构建右子树
        root.right = build(inorder, index + 1, inEnd, postorder, postStart + leftSize , postEnd - 1);
        return root;
    }

}
// @lc code=end

