#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        
        head.next = None
        return new_head
            
        
# @lc code=end

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
new_head = Solution().reverseList(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next