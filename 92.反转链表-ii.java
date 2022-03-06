/*
 * @lc app=leetcode.cn id=92 lang=java
 *
 * [92] 反转链表 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    // 标记最后节点指向
    public static ListNode s = null;

    /**
     * 逆转链表前N个元素
     * 
     * @param head
     * @param n
     * @return
     */
    public static ListNode reverseTopN(ListNode head, int n) {
        if (n == 1) {
            // 记录逆转结尾处的下一个节点
            s = head.next;
            return head;
        }
        ListNode last = reverseTopN(head.next, n - 1);
        head.next.next = head;
        head.next = s;
        return last;
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        // 如果左区间为1，那么相当于逆转前N个节点
        if (left == 1) {
            return reverseTopN(head, right);
        }
        // 递归，右移一个节点，直到左区间为1
        head.next = reverseBetween(head.next, left - 1, right - 1);
        return head;
    }
}
// @lc code=end
