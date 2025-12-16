#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        def reverse(head: ListNode):
            pre = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = pre
                pre = curr
                curr = next_node
            return pre
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        end = dummy
        
        while end.next:
            
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            
            start = pre.next
            next_group = end.next
            end.next = None
            
            pre.next = reverse(start)
            
            start.next = next_group
            
            pre = start
            end = pre
        return dummy.next
            
            
        
        
        
# @lc code=end
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
print(Solution().reverseKGroup(head, k))