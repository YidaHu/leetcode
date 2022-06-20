import com.sun.org.apache.xalan.internal.xsltc.runtime.Node;

/*
 * @lc app=leetcode.cn id=116 lang=java
 *
 * [116] 填充每个节点的下一个右侧节点指针
 */

// @lc code=start

/* // Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}; */

class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return null;
        }
        twoNodeConnect(root.left, root.right);
        return root;
    }

    public void twoNodeConnect(Node node1, Node node2) {
        if (node1 == null || node2 == null) {
            return;
        }
        // 前序遍历位置
        // 将传入的两个节点连接
        node1.next = node2;
        // 相同父节点，左右相连
        twoNodeConnect(node1.left, node1.right);
        twoNodeConnect(node2.left, node2.right);
        // 不同父节点，左右相连
        twoNodeConnect(node1.right, node2.left);
    }
}
// @lc code=end
