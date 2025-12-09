#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 1. 造一个假头，作为新链表的起点
        dummy = ListNode(-1)
        curr = dummy  # 施工队长，负责把后面的节点一个个接起来
        
        # 2. 只要两个链表都有货，就比大小
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1   # list1 小，接 list1
                list1 = list1.next  # list1 往前走一步
            else:
                curr.next = list2   # list2 小，接 list2
                list2 = list2.next  # list2 往前走一步
            
            curr = curr.next        # 施工队长往前走一步，准备接下一个
            
        # 3. 收尾：肯定有一个链表先空，另一个还没空
        # 因为剩下的部分本身就是有序的，直接把整串接过来就行
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        # 4. 返回假头的下一个，才是真头
        return dummy.next
        
        
# @lc code=end

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
merged_head = Solution().mergeTwoLists(list1, list2)
while merged_head:
    print(merged_head.val)
    merged_head = merged_head.next