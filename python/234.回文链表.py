#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(head_: ListNode):
            pre = None
            curr = head_
            while curr:
                next_node = curr.next
                curr.next = pre
                pre = curr
                curr = next_node
            return pre
        left = head
        right = reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
# @lc code=end

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
sol = Solution()
print(sol.isPalindrome(head))  # True