//<p>给定一个非负整数&nbsp;<code>c</code>&nbsp;，你要判断是否存在两个整数 <code>a</code> 和 <code>b</code>，使得&nbsp;<code>a<sup>2</sup> + b<sup>2</sup> = c</code> 。</p>
//
//<p>&nbsp;</p>
//
//<p><strong>示例 1：</strong></p>
//
//<pre>
//<strong>输入：</strong>c = 5
//<strong>输出：</strong>true
//<strong>解释：</strong>1 * 1 + 2 * 2 = 5
//</pre>
//
//<p><strong>示例 2：</strong></p>
//
//<pre>
//<strong>输入：</strong>c = 3
//<strong>输出：</strong>false
//</pre>
//
//<p>&nbsp;</p>
//
//<p><strong>提示：</strong></p>
//
//<ul> 
// <li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li> 
//</ul>
//
//<div><div>Related Topics</div><div><li>数学</li><li>双指针</li><li>二分查找</li></div></div><br><div><li>👍 412</li><li>👎 0</li></div>
/**
 * @author YidaHu
 */
package leetcode.editor.cn;

class Solution633 {
    public static void main(String[] args) {
        Solution solution = new Solution633().new Solution();
        System.out.println(solution.judgeSquareSum(4));
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public boolean judgeSquareSum(int c) {
            if (c == 0) {
                return true;
            }
            int i = 0, j = (int) (Math.sqrt(c));
            while (i <= j) {
                if (Math.pow(i, 2) + Math.pow(j, 2) == c) {
                    return true;
                } else if (c - Math.pow(i, 2) < Math.pow(j, 2)) {
                    j--;
                } else {
                    i++;
                }
            }
            return false;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}

