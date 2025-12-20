#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head
        # 修正：必须先判断 fast 和 fast.next 是否存在
        # 因为 fast 跑得快，如果 fast 跑到 None 了，访问 fast.next 就会报错
        # 如果 fast.next 是 None，访问 fast.next.next 也会报错
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# @lc code=end
head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next  # 创建环
print(Solution().hasCycle(head))
