/*
 * @lc app=leetcode.cn id=785 lang=java
 *
 * [785] 判断二分图
 */

// @lc code=start
class Solution {


    public boolean ok = true;
    public boolean[] visited;
    public boolean[] color;

    public boolean isBipartite(int[][] graph) {
        int len = graph.length;
        visited = new boolean[len];
        color = new boolean[len];
        // 遍历图
        for (int v = 0; v < len; v++) {
            if (!visited[v]) {
                traverse(graph, v);
            }
        }
        return ok;

    }

    /**
     * DFS遍历
     * @param graph
     * @param v
     */
    public void traverse(int[][] graph, int v) {
        if (!ok) {
            return;
        }
        visited[v] = true;
        for (int i : graph[v]) {
            if (!visited[i]) {
                // 相邻节点没有被访问，涂上不同的颜色
                color[i] = !color[v];
                traverse(graph, i);
            } else {
                // 相邻节点已经被访问，且颜色一样，那么不是二分图
                if (color[i] == color[v]) {
                    ok = false;
                }
            }
        }


    }

}
// @lc code=end

