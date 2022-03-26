import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=797 lang=java
 *
 * [797] 所有可能的路径
 */

// @lc code=start
class Solution {

    List<List<Integer>> res = new LinkedList<>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        LinkedList<Integer> path = new LinkedList<>();
        traverse(graph, 0, path);
        return res;
    }

    /**
     * 
     * @param graph 领结表
     * @param s 节点
     * @param path  路径
     * @return
     */
    public void traverse(int[][] graph, int s, LinkedList<Integer> path) {
        // 进来，把节点添加到路径
        path.addLast(s);
        // 获得图的长度
        int n = graph.length;
        // 判断当前节点是否达到图的长度
        if (s == n - 1) {
            res.add(new LinkedList<>(path));
            path.removeLast();
            return;
        }
        // 遍历领结点
        for (int v : graph[s]) {
            traverse(graph, v, path);
        }

        // 出去，把节点移出路径
        path.removeLast();
        return;
    }
}
// @lc code=end

