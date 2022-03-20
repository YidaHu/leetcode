import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode.cn id=652 lang=java
 *
 * [652] 寻找重复的子树
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

    HashMap<String, Integer> count = new HashMap<>();
    List<TreeNode> res = new ArrayList();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        count(root);
        return res;
    }

    public String count(TreeNode root) {
        if (root == null) {
            return "#";
        }
        String left = count(root.left);
        String right = count(root.right);
        String serial = left + "," + right + "," + root.val;
        count.put(serial, count.getOrDefault(serial, 0) + 1);
        if (count.get(serial) == 2) {
            res.add(root);
        }
        return serial;
    }

}
// @lc code=end

