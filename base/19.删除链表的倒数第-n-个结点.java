import java.util.List;

/*
 * @lc app=leetcode.cn id=19 lang=java
 *
 * [19] 删除链表的倒数第 N 个结点
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

    public ListNode findFromEnd(ListNode head, int n) {
        ListNode p = head;
        for (int i = 0; i < n; i++) {
            p = p.next;
        }
        ListNode p1 = head;
        while (p != null) {
            p = p.next;
            p1 = p1.next;
        }
        return p1;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 虚拟节点
        ListNode dummy = new ListNode(-1, head);
        // 获取链表长度
        int lenght = 0;
        while (head != null) {
            ++lenght;
            head = head.next;
        }
        // 找到第n个前驱节点
        ListNode p = dummy;
        for (int i = 1; i < lenght - n + 1; i++) {
            p = p.next;
        }
        // 删除第n个节点
        p.next = p.next.next;
        ListNode res = dummy.next;
        return res;

    }
}
// @lc code=end
