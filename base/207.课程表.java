import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode.cn id=207 lang=java
 *
 * [207] 课程表
 */

// @lc code=start
class Solution {

    List<Integer>[] graph;
    boolean[] visited;
    boolean[] onPath;
    boolean hasCycle = false;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            traverse(graph, i);
        }
        return !hasCycle;
    }

    /**
     * 遍历图
     * @param graph
     * @param s
     */
    public void traverse(List<Integer>[] graph, int s) {
        // 如果已经此在路径上，说明有环
        if (onPath[s]) {
            hasCycle = true;
        }
        // 已经走过或着有环
        if (visited[s] || hasCycle) {
            return;
        }
        // 进入节点，添加
        visited[s] = true;
        onPath[s] = true;
        // 遍历图中的路径
        for (int t : graph[s]) {
            traverse(graph, t);
        }
        // 走完此次路径，移出
        onPath[s] = false;

    }

    /**
     * 构建图
     * @param numCourses
     * @param prerequisites
     * @return
     */
    public List<Integer>[] buildGraph(int numCourses, int[][] prerequisites) {
        graph = new LinkedList[numCourses];
        // 初始化
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new LinkedList<>();
        }
        // 遍历边
        for(int[] edges: prerequisites) {
            int from = edges[0];
            int to = edges[1];
            graph[from].add(to);
        }
        return graph;
    }
}
// @lc code=end

