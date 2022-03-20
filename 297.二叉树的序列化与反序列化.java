import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode.cn id=297 lang=java
 *
 * [297] 二叉树的序列化与反序列化
 */

// @lc code=start

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Codec {

    String SEP = ",";
    String NULL = "#";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        rSerialize(root, sb);
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] datas = data.split(SEP);
        List<String> list = new LinkedList<String>(Arrays.asList(datas));
        return rDeserialize(list);
    }

    public void rSerialize(TreeNode root, StringBuilder sb) {
        if (root == null) {
            // 如果空，添加#,
            sb.append(NULL).append(SEP);
        } else {
            // 根。添加“值,”
            sb.append(root.val).append(SEP);
            // 左子树
            rSerialize(root.left, sb);
            // 右子树
            rSerialize(root.right, sb);
        }
    }

    public TreeNode rDeserialize(List<String> list) {
        // 如果为空，删除，返回
        if (list.get(0).equals(NULL)) {
            list.remove(0);
            return null;
        }
        // 添加根
        TreeNode root = new TreeNode(Integer.parseInt(list.get(0)));
        // 添加后删除
        list.remove(0);
        // 左子树
        root.left = rDeserialize(list);
        // 右子树
        root.right = rDeserialize(list);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// @lc code=end

