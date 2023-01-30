//<p>给你两个链表&nbsp;<code>list1</code> 和&nbsp;<code>list2</code>&nbsp;，它们包含的元素分别为&nbsp;<code>n</code> 个和&nbsp;<code>m</code> 个。</p>
//
//<p>请你将&nbsp;<code>list1</code>&nbsp;中下标从 <code>a</code> 到 <code>b</code> 的全部节点都删除，并将<code>list2</code>&nbsp;接在被删除节点的位置。</p>
//
//<p>下图中蓝色边和节点展示了操作后的结果：</p> 
//<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/fig1.png" style="height: 130px; width: 504px;" /> 
//<p>请你返回结果链表的头指针。</p>
//
//<p>&nbsp;</p>
//
//<p><strong>示例 1：</strong></p>
//
//<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex1.png" style="width: 406px; height: 140px;" /></p>
//
//<pre>
//<b>输入：</b>list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
//<b>输出：</b>[0,1,2,1000000,1000001,1000002,5]
//<b>解释：</b>我们删除 list1 中下标为 3 和 4 的两个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
//</pre>
//
//<p><strong>示例 2：</strong></p> 
//<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex2.png" style="width: 463px; height: 140px;" /> 
//<pre>
//<b>输入：</b>list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
//<b>输出：</b>[0,1,1000000,1000001,1000002,1000003,1000004,6]
//<b>解释：</b>上图中蓝色的边和节点为答案链表。
//</pre>
//
//<p>&nbsp;</p>
//
//<p><strong>提示：</strong></p>
//
//<ul> 
// <li><code>3 &lt;= list1.length &lt;= 10<sup>4</sup></code></li> 
// <li><code>1 &lt;= a &lt;= b &lt; list1.length - 1</code></li> 
// <li><code>1 &lt;= list2.length &lt;= 10<sup>4</sup></code></li> 
//</ul>
//
//<div><div>Related Topics</div><div><li>链表</li></div></div><br><div><li>👍 85</li><li>👎 0</li></div>
/**
 * @author YidaHu
 */
package leetcode.editor.cn;


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution1669 {
    public static void main(String[] args) {
        Solution solution = new Solution1669().new Solution();
    }
    //leetcode submit region begin(Prohibit modification and deletion)


    class Solution {
        public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
            ListNode preA = list1;
            for (int i = 0; i < a - 1; i++) {
                preA = preA.next;
            }
            ListNode aftB = preA;
            for (int i = 0; i < b - a + 2; i++) {
                aftB = aftB.next;
            }
            preA.next = list2;
            while (list2.next != null) {
                list2 = list2.next;
            }
            list2.next = aftB;
            return list1;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}

