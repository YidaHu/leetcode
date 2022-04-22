import java.util.Deque;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

import com.sun.org.apache.bcel.internal.classfile.Node;

/*
 * @lc app=leetcode.cn id=429 lang=java
 *
 * [429] N 叉树的层序遍历
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {

    List<List<Integer>> result = new ArrayList<List<Integer>>();

    public List<List<Integer>> levelOrder(Node root) {
        traverse(root);
        return result;
    }

    public void traverse(Node root) {
        if (root == null) {
            return;
        }
        Deque<Node> q = new ArrayDeque<>();
        q.addLast(root);
        while(!q.isEmpty()) {
            int size = q.size();
            List<Integer> n = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                Node current = q.removeFirst();
                n.add(current.val);
                for (Node node : current.children) {
                    q.addLast(node);
                }
            }
            result.add(n);
        }
    }

}
// @lc code=end

