//<p>在一个有向图中，节点分别标记为&nbsp;<code>0, 1, ..., n-1</code>。图中每条边为红色或者蓝色，且存在自环或平行边。</p>
//
//<p><code>red_edges</code>&nbsp;中的每一个&nbsp;<code>[i, j]</code>&nbsp;对表示从节点 <code>i</code> 到节点 <code>j</code> 的红色有向边。类似地，<code>blue_edges</code>&nbsp;中的每一个&nbsp;<code>[i, j]</code>&nbsp;对表示从节点 <code>i</code> 到节点 <code>j</code> 的蓝色有向边。</p>
//
//<p>返回长度为 <code>n</code> 的数组&nbsp;<code>answer</code>，其中&nbsp;<code>answer[X]</code>&nbsp;是从节点&nbsp;<code>0</code>&nbsp;到节点&nbsp;<code>X</code>&nbsp;的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 <code>answer[x] = -1</code>。</p>
//
//<p>&nbsp;</p>
//
//<p><strong>示例 1：</strong></p>
//
//<pre>
//<strong>输入：</strong>n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
//<strong>输出：</strong>[0,1,-1]
//</pre>
//
//<p><strong>示例 2：</strong></p>
//
//<pre>
//<strong>输入：</strong>n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
//<strong>输出：</strong>[0,1,-1]
//</pre>
//
//<p><strong>示例 3：</strong></p>
//
//<pre>
//<strong>输入：</strong>n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
//<strong>输出：</strong>[0,-1,-1]
//</pre>
//
//<p><strong>示例 4：</strong></p>
//
//<pre>
//<strong>输入：</strong>n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
//<strong>输出：</strong>[0,1,2]
//</pre>
//
//<p><strong>示例 5：</strong></p>
//
//<pre>
//<strong>输入：</strong>n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
//<strong>输出：</strong>[0,1,1]
//</pre>
//
//<p>&nbsp;</p>
//
//<p><strong>提示：</strong></p>
//
//<ul> 
// <li><code>1 &lt;= n &lt;= 100</code></li> 
// <li><code>red_edges.length &lt;= 400</code></li> 
// <li><code>blue_edges.length &lt;= 400</code></li> 
// <li><code>red_edges[i].length == blue_edges[i].length == 2</code></li> 
// <li><code>0 &lt;= red_edges[i][j], blue_edges[i][j] &lt; n</code></li> 
//</ul>
//
//<div><div>Related Topics</div><div><li>广度优先搜索</li><li>图</li></div></div><br><div><li>👍 236</li><li>👎 0</li></div>
/**
 * @author YidaHu
 */
package leetcode.editor.cn;

import java.util.*;

class Solution1129 {
    public static void main(String[] args) {
        Solution solution = new Solution1129().new Solution();
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
            List<Integer>[][] g = new List[2][n];
            for (var f : g) {
                Arrays.setAll(f, k -> new ArrayList<>());
            }
            for (var e : redEdges) {
                g[0][e[0]].add(e[1]);
            }
            for (var e : blueEdges) {
                g[1][e[0]].add(e[1]);
            }
            Deque<int[]> q = new ArrayDeque<>();
            q.offer(new int[]{0, 0});
            q.offer(new int[]{0, 1});
            boolean[][] vis = new boolean[n][2];
            int[] ans = new int[n];
            Arrays.fill(ans, -1);
            int d = 0;
            while (!q.isEmpty()) {
                for (int k = q.size(); k > 0; --k) {
                    var p = q.poll();
                    int i = p[0], c = p[1];
                    if (ans[i] == -1) {
                        ans[i] = d;
                    }
                    vis[i][c] = true;
                    c ^= 1;
                    for (int j : g[c][i]) {
                        if (!vis[j][c]) {
                            q.offer(new int[]{j, c});
                        }
                    }
                }
                ++d;
            }
            return ans;
        }


    }
//leetcode submit region end(Prohibit modification and deletion)
}


