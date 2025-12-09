#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        curr = dummy
        temp = 0
        # 循环条件：只要 l1 没走完，或者 l2 没走完，或者还有进位没处理
        while l1 or l2 or temp:
            # 1. 安全取值：如果节点空了就当 0
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            # 2. 求和：两个数 + 进位
            total = a + b + temp
            
            # 3. 算进位和个位
            temp = total // 10  # 进位 (15 -> 1)
            digit = total % 10  # 个位 (15 -> 5)
            
            # 4. 接到新链表后面
            curr.next = ListNode(digit)
            curr = curr.next
            
            # 5. 指针后移
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

        
# @lc code=end

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result_head = Solution().addTwoNumbers(l1, l2)
while result_head:
    print(result_head.val)
    result_head = result_head.next