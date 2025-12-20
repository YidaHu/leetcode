#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针法 (Floyd's Cycle-Finding Algorithm)
        slow = head
        fast = head
        
        # 第一阶段：判断是否有环
        while True:
            # 如果快指针走到头了，说明没有环
            if not (fast and fast.next):
                return None
            
            slow = slow.next
            fast = fast.next.next
            
            # 如果相遇，说明有环，退出循环进入第二阶段
            if slow == fast:
                break
        
        # 第二阶段：寻找环的入口
        # 数学证明：
        # 设头节点到环入口距离为 x
        # 环入口到相遇点距离为 y
        # 环剩余长度为 z (即相遇点回到环入口的距离)
        # 
        # 相遇时：
        # 慢指针走了：x + y
        # 快指针走了：x + y + n * (y + z)  (n为圈数)
        # 
        # 因为快指针速度是慢指针的2倍：
        # 2 * (x + y) = x + y + n * (y + z)
        # x + y = n * (y + z)
        # x = n * (y + z) - y
        # x = (n - 1) * (y + z) + z
        # 
        # 当 n=1 时，x = z。这意味着：
        # 从头节点出发一个指针，从相遇点出发一个指针，
        # 它们同时每次走一步，最终会在环入口相遇。
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow

        
        
# @lc code=end
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # 创建环
print(Solution().detectCycle(head))
