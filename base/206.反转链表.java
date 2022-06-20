/*
 * @lc app=leetcode.cn id=206 lang=java
 *
 * [206] 反转链表
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

    // /**
    // * 1. 迭代遍历法
    // *
    // * @param head
    // * @return
    // */
    // public ListNode reverseList(ListNode head) {
    // if (head == null)
    // return null;
    // ListNode pre = head;
    // ListNode cur = head.next;
    // ListNode temp;
    // while (cur != null) {
    // temp = cur.next;
    // cur.next = pre;
    // pre = cur;
    // cur = temp;
    // }
    // head.next = null;
    // return pre;
    // }

    /**
     * 递归
     * 
     * @param head
     * @return
     */
    public ListNode reverseList(ListNode head) {
        // 链表只有一个节点时，返回自身
        if (head == null || head.next == null) {
            return head;
        }
        ListNode last = reverseList(head.next);
        // 节点指向反转
        head.next.next = head;
        // 链表结尾指向null
        head.next = null;
        return last;
    }
}
// @lc code=end
