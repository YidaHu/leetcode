import java.util.Collections;
import java.util.List;

/*
 * @lc app=leetcode.cn id=210 lang=java
 *
 * [210] 课程表 II
 */

// @lc code=start
class Solution {

    List<Integer>[] graph;
    boolean[] visited;
    boolean[] onPath;
    boolean hasCycle = false;
    List<Integer> postOrder = new ArrayList<Integer>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            traverse(graph, i);
        }
        if (hasCycle) {
            return new int[]{};
        }
        // Collections.reverse(postOrder);
        int[] res = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            res[i] = postOrder.get(i);
        }
        return res;

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
        // 后序遍历位置
        postOrder.add(s);
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

