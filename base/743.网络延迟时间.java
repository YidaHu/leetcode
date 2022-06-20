import java.awt.List;
import java.util.Arrays;
import java.util.Queue;

/*
 * @lc app=leetcode.cn id=743 lang=java
 *
 * [743] 网络延迟时间
 */

// @lc code=start

public class State {

  private int id;
  private int distFromStart;

  public State(int id, int distFromStart) {
    this.id = id;
    this.distFromStart = distFromStart;
  }
}

class Solution {

  public int networkDelayTime(int[][] times, int n, int k) {}

  public int[] dijkstra(int start, List graph) {
    // distTo[i] 就是start到目标i的最短路径权重
    int[] distTo = new int[graph.length];
    // 初始化
    Arrays.fill(distTo, Integer.MAX_VALUE);
    // distTo的start到start为0
    distTo[start] = 0;
    Queue<State> pq = new PriorityQueue<>(
      (a, b) -> {
        return a.distFromStart - b.distFromStart;
      }
    );
  }
}
// @lc code=end
