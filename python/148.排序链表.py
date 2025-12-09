#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        题目解析：
        对链表进行排序，要求时间复杂度 O(n log n)。
        最适合链表的排序算法是【归并排序】(Merge Sort)。
        
        核心思想（分治法）：
        1. 分 (Divide)：把链表从中间切断，分成两半。递归地重复这个过程，直到每个链表只剩 1 个节点。
        2. 治 (Conquer)：把两个已经有序的链表合并成一个有序链表。
        """
        # 1. 递归终止条件 (Base Case)
        # 如果链表为空，或者只有一个节点，说明它已经是有序的了，直接返回。
        # 这里的 head.next is None 就是判断是否只剩一个节点。
        if not head or head.next is None:
            return head
            
        # 2. 找中点 (Find Middle)
        # 使用【快慢指针】技巧：
        # slow 一次走一步，fast 一次走两步。
        # 当 fast 走到末尾时，slow 刚好走到中间。
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # mid 就是右半部分的头节点
        mid = slow.next
        # 3. 断开链表 (Cut)
        # 这一步非常关键！必须把左半部分和右半部分断开。
        # slow.next = None 相当于切断了中间的连接。
        slow.next = None

        # 4. 递归排序 (Recursive Sort)
        # 对左半部分 (head) 进行排序
        left = self.sortList(head)
        # 对右半部分 (mid) 进行排序
        right = self.sortList(mid)
        
        # 5. 合并 (Merge)
        # 将排好序的左右两部分合并
        return self.merge(left, right)

    def merge(self, left, right):
        """
        合并两个有序链表
        原理：双指针法，谁小选谁，串起来。
        """
        # 创建一个虚拟头节点 (Dummy Node)
        # 它的作用是作为新链表的“桩”，方便我们往后接节点。
        # dummy.val 是多少不重要，因为最后返回的是 dummy.next
        dummy = ListNode(0)
        # curr 指针用来指向当前新链表的末尾
        curr = dummy
        
        # 当两个链表都还有节点时，进行比较
        while left and right:
            if left.val < right.val:
                # 如果左边的节点值小，就把 curr 的 next 指向左边这个节点
                curr.next = left
                # 左边指针后移
                left = left.next
            else:
                # 如果右边的节点值小，就把 curr 的 next 指向右边这个节点
                curr.next = right
                # 右边指针后移
                right = right.next
            # curr 指针也必须后移，准备接下一个节点
            curr = curr.next
            
        # 处理剩余节点
        # 如果其中一个链表先走完了，另一个链表剩下的部分直接接在后面即可
        # 因为剩下的部分本身就是有序的
        if left:
            curr.next = left
        if right:
            curr.next = right
            
        # 返回虚拟头节点的下一个节点，这才是真正的有序链表头
        return dummy.next


# @lc code=end

head = ListNode(4, ListNode(2, ListNode(1)))
sorted_head = Solution().sortList(head)
while sorted_head:
    print(sorted_head.val, end=' -> ')
    sorted_head = sorted_head.next
print('None')
