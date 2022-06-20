import java.util.Collection;
import java.util.Collections;
import java.util.List;

/*
 * @lc app=leetcode.cn id=1584 lang=java
 *
 * [1584] 连接所有点的最小费用
 */

// @lc code=start
public class UF {

  // 记录连通分量
  private int count;
  // 节点x的parent是parent[x]
  private int[] parent;
  // 树的重量
  private int[] size;

  // 构造函数
  public UF(int n) {
    this.count = n;
    parent = new int[n];
    size = new int[n];
    for (int i = 0; i < n; i++) {
      parent[i] = i;
      size[i] = 1;
    }
  }

  /**
   * 连通
   * @param p
   * @param q
   */
  public void union(int p, int q) {
    int rootP = findRoot(p);
    int rootQ = findRoot(q);
    if (rootP == rootQ) {
      return;
    }
    // 将两个数合并为一颗树
    parent[rootP] = rootQ;

    // 平衡树，小树接到大树下面
    if (size[rootP] > size[rootQ]) {
      parent[rootQ] = rootP;
      size[rootQ] += size[rootP];
    } else {
      parent[rootP] = rootQ;
      size[rootP] += size[rootQ];
    }

    // 连通分量减一
    count--;
  }

  /**
   * 是否连通
   * @param p
   * @param q
   * @return
   */
  public boolean connected(int p, int q) {
    int rootP = findRoot(p);
    int rootQ = findRoot(q);
    return rootP == rootQ;
  }

  /**
   * 获取连通分量
   * @return
   */
  public int count() {
    return count;
  }

  /**
   * 发现根节点
   * @param x
   * @return
   */
  public int findRoot(int x) {
    // 根节点的parent[x] == x
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }
}

class Solution {

  public int minCostConnectPoints(int[][] points) {
    int n = points.length;
    List<int[]> edges = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int xi = points[i][0];
        int yi = points[i][1];
        int xj = points[j][0];
        int yj = points[j][1];
        edges.add(new int[] { i, j, Math.abs(xi - xj) + Math.abs(yi - yj) });
      }
    }

    // 将变的权重按从小到大排序
    Collections.sort(
      edges,
      (a, b) -> {
        return a[2] - b[2];
      }
    );
    // 执行Kruskal算法
    int mst = 0;
    UF uf = new UF(n);
    for (int[] edge : edges) {
      int u = edge[0];
      int v = edge[1];
      int weight = edge[2];
      if (uf.connected(u, v)) {
        continue;
      }
      mst += weight;
      uf.union(u, v);
    }
    return mst;
  }
}
// @lc code=end
