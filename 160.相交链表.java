/*
 * @lc app=leetcode.cn id=160 lang=java
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */
public class Solution {

    // /**
    // * 1. 暴力破解法
    // *
    // * @param headA
    // * @param headB
    // * @return
    // */
    // public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    // while (headA != null) {
    // ListNode node = headB;
    // while (node != null) {
    // if (headA == node) {
    // return node;
    // }
    // node = node.next;
    // }
    // headA = headA.next;
    // }
    // return null;
    // }

    /**
     * 双指针
     * 
     * @param headA
     * @param headB
     * @return
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA, p2 = headB;
        while (p1 != p2) {
            // p1走完A链表转到B链表
            if (p1 == null)
                p1 = headB;
            else
                p1 = p1.next;
            // p2走完B链表转到A链表
            if (p2 == null)
                p2 = headA;
            else
                p2 = p2.next;
        }
        return p1;
    }
}
// @lc code=end
