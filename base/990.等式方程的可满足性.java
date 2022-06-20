/*
 * @lc app=leetcode.cn id=990 lang=java
 *
 * [990] 等式方程的可满足性
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

  public boolean equationsPossible(String[] equations) {
    UF uf = new UF(26);
    // 先处理==的连通
    for (String equation : equations) {
      if (equation.charAt(1) == '=') {
        char x = equation.charAt(0);
        char y = equation.charAt(3);
        uf.union(x - 'a', y - 'a');
      }
    }
    // 再检查不连通
    for (String equation : equations) {
      if (equation.charAt(1) == '!') {
        char x = equation.charAt(0);
        char y = equation.charAt(3);
        boolean isConnection = uf.connected(x - 'a', y - 'a');
        if (isConnection) {
          return false;
        }
      }
    }
    return true;
  }
}
// @lc code=end
