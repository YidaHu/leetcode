/*
 * @lc app=leetcode.cn id=130 lang=java
 *
 * [130] 被围绕的区域
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

  public void solve(char[][] board) {
    if (board.length == 0) return;
    int m = board.length;
    int n = board[0].length;
    // dummy
    UF uf = new UF(m * n + 1);
    int dummy = m * n;
    // 首列和末列为0的与dummy连通
    for (int i = 0; i < m; i++) {
      if (board[i][0] == 'O') uf.union(i * n, dummy);
      if (board[i][n - 1] == 'O') uf.union(i * n + n - 1, dummy);
    }
    // 首行与末行为0的与dummy连通
    for (int j = 0; j < n; j++) {
      if (board[0][j] == 'O') uf.union(j, dummy);
      if (board[m - 1][j] == 'O') uf.union(n * (m - 1) + j, dummy);
    }
    int[][] d = new int[][] { { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, 0 } };
    for (int i = 1; i < m - 1; i++) {
      for (int j = 1; j < n - 1; j++) {
        if (board[i][j] == 'O') {
          for (int k = 0; k < 4; k++) {
            int x = i + d[k][0];
            int y = j + d[k][1];
            if (board[x][y] == 'O') uf.union(x * n + y, i * n + j);
          }
        }
      }
    }
    for (int i = 1; i < m - 1; i++) {
      for (int j = 1; j < n - 1; j++) {
        if (!uf.connected(dummy, i * n + j)) board[i][j] = 'X';
      }
    }
  }
}
// @lc code=end
