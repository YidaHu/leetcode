import java.util.Queue;

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
        for (int i = 0; i < len; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        return ok;
    }

    /**
     * BFS遍历
     * @param graph
     * @param start
     */
    public void traverse(int[][] graph, int start) {

        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(start);
        visited[start] = true;
        while (!q.isEmpty() && ok) {
            int v = q.poll();
            for (int i : graph[v]) {
                if (!visited[i]) {
                    color[i] = !color[v];
                    q.offer(i);
                    visited[i] = true;
                } else {
                    if (color[i] == color[v]) {
                        ok = false;
                    }
                }
            }
        }
    }
}
// @lc code=end

