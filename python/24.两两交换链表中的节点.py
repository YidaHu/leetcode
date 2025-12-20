#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    
class Solution(object):
    def swapPairs(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            curr = prev.next
            next_ = curr.next
            
            prev.next = next_
            curr.next = next_.next
            next_.next = curr
            prev = curr
        
        return dummy.next
        
        
# @lc code=end
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
new_head = Solution().swapPairs(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next
