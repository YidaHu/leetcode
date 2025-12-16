# LeetCode 刷题速查表 (Cheat Sheet)

## 1. 堆 (Heap)
*   **关键词**：“Top K”、“第 K 大/小”
*   **口诀**：找最大用小顶堆，找最小用大顶堆。
*   **核心库**：`import heapq` (默认小顶堆)

```python
import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num) # 入堆
        if len(heap) > k:
            heapq.heappop(heap)   # 维护堆大小为 K
    return heap[0] # 堆顶就是第 K 大
```

## 2. BFS (广度优先搜索)
*   **关键词**：“最短路径”、“最少步数”、“层序遍历”、“最近”、“同时扩散”
*   **核心结构**：`Queue` (队列) + `While` 循环
*   **适用**：腐烂橘子、迷宫最短路

```python
from collections import deque

def bfs(grid):
    queue = deque([(0, 0)]) # 起点入队
    visited = set([(0, 0)]) # 记录访问
    step = 0
    
    while queue:
        size = len(queue) # 锁定当前层
        for _ in range(size):
            r, c = queue.popleft()
            if target_found: return step
            
            # 向四周扩散
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        step += 1
    return -1
```

## 3. DFS (回溯/递归)
*   **关键词**：“所有组合”、“所有排列”、“所有路径”、“是否存在路径”
*   **核心结构**：递归 + 循环 + 撤销选择 (Backtrack)
*   **适用**：全排列、组合总和、岛屿数量

```python
def permute(nums):
    res = []
    def backtrack(path, used):
        if len(path) == len(nums): # 结束条件
            res.append(path[:])    # ⚠️ 拷贝路径
            return
        
        for i in range(len(nums)):
            if used[i]: continue   # 剪枝
            
            path.append(nums[i])   # 做选择
            used[i] = True
            
            backtrack(path, used)  # 进入下一层
            
            path.pop()             # 撤销选择
            used[i] = False
            
    backtrack([], [False] * len(nums))
    return res
```

## 4. 滑动窗口 (Sliding Window)
*   **关键词**：“连续子数组”、“子串”
*   **特征**：窗口忽大忽小，像毛毛虫一样爬。
*   **适用**：无重复字符最长子串、长度最小的子数组

```python
def lengthOfLongestSubstring(s):
    window = {}
    left = 0
    ans = 0
    
    for right in range(len(s)):
        # 1. 进窗口
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        # 2. 出窗口 (当条件不满足时，比如有重复字符)
        while window[char] > 1:
            d = s[left]
            window[d] -= 1
            left += 1
            
        # 3. 更新结果
        ans = max(ans, right - left + 1)
    return ans
```

## 5. 二分查找 (Binary Search)
*   **关键词**：“有序数组”、“查找某个值”、“时间复杂度 O(log N)”
*   **模版**：`left, right = 0, n-1`，`while left <= right`

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 6. 链表 (Linked List)
*   **关键词**：“链表操作”、“反转”、“合并”、“环”
*   **技巧**：双指针（快慢指针）、虚拟头节点 (Dummy Head)
*   **注意**：遇到链表题，先画图，别空想。

```python
# 虚拟头节点模版 (解决头节点可能变化的问题)
def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    curr = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 if l1 else l2
    return dummy.next
```

## 7. 二叉树 (Binary Tree)
*   **关键词**：“二叉树”、“深度”、“路径”
*   **核心**：递归 (Recursive)
*   **心法**：问自己——我要从左子树拿什么？从右子树拿什么？怎么拼凑出答案？

```python
# 递归模版 (求最大深度)
def maxDepth(root):
    if not root:
        return 0
    
    # 1. 问左子树要深度
    left_depth = maxDepth(root.left)
    # 2. 问右子树要深度
    right_depth = maxDepth(root.right)
    
    # 3. 加上自己这一层
    return max(left_depth, right_depth) + 1
```
