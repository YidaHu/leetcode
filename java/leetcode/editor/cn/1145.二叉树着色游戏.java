//<p>有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点&nbsp;<code>root</code>，树上总共有 <code>n</code> 个节点，且 <code>n</code> 为奇数，其中每个节点上的值从&nbsp;<code>1</code> 到&nbsp;<code>n</code>&nbsp;各不相同。</p>
//
//<p>最开始时：</p>
//
//<ul> 
// <li>「一号」玩家从 <code>[1, n]</code>&nbsp;中取一个值&nbsp;<code>x</code>（<code>1 &lt;= x &lt;= n</code>）；</li> 
// <li>「二号」玩家也从&nbsp;<code>[1, n]</code>&nbsp;中取一个值&nbsp;<code>y</code>（<code>1 &lt;= y &lt;= n</code>）且&nbsp;<code>y != x</code>。</li> 
//</ul>
//
//<p>「一号」玩家给值为&nbsp;<code>x</code>&nbsp;的节点染上红色，而「二号」玩家给值为&nbsp;<code>y</code>&nbsp;的节点染上蓝色。</p>
//
//<p>之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 <strong>未着色 </strong>的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。</p>
//
//<p>如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。</p>
//
//<p>若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。</p>
//
//<p>现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个&nbsp;<code>y</code>&nbsp;值可以确保你赢得这场游戏，则返回&nbsp;<code>true</code> ；若无法获胜，就请返回 <code>false</code> 。</p> &nbsp;
//
//<p><strong class="example">示例 1 ：</strong></p> 
//<img alt="" src="https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png" style="width: 500px; height: 310px;" /> 
//<pre>
//<strong>输入：</strong>root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
//<strong>输出：</strong>true
//<strong>解释：</strong>第二个玩家可以选择值为 2 的节点。</pre>
//
//<p><strong class="example">示例 2 ：</strong></p>
//
//<pre>
//<strong>输入：</strong>root = [1,2,3], n = 3, x = 1
//<strong>输出：</strong>false
//</pre>
//
//<p>&nbsp;</p>
//
//<p><strong>提示：</strong></p>
//
//<ul> 
// <li>树中节点数目为 <code>n</code></li> 
// <li><code>1 &lt;= x &lt;= n &lt;= 100</code></li> 
// <li><code>n</code> 是奇数</li> 
// <li><code>1 &lt;= Node.val &lt;= n</code></li> 
// <li>树中所有值 <strong>互不相同</strong></li> 
//</ul>
//
//<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div><br><div><li>👍 185</li><li>👎 0</li></div>
/**
 * @author YidaHu
 */
package leetcode.editor.cn;

class Solution1145 {
    public static void main(String[] args) {
        Solution solution = new Solution1145().new Solution();
    }
    //leetcode submit region begin(Prohibit modification and deletion)

    /**
     * Definition for a binary tree node.
     * public class TreeNode {
     * int val;
     * TreeNode left;
     * TreeNode right;
     * TreeNode() {}
     * TreeNode(int val) { this.val = val; }
     * TreeNode(int val, TreeNode left, TreeNode right) {
     * this.val = val;
     * this.left = left;
     * this.right = right;
     * }
     * }
     */

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    class Solution {
        public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
            return false;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}

