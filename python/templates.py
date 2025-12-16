# ==========================================
# 1. 二分查找 (Binary Search)
# ==========================================
# 适用场景：有序数组查找、寻找边界
# 时间复杂度：O(log N)
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # 找到了
        elif nums[mid] < target:
            left = mid + 1  # 在右半边
        else:
            right = mid - 1  # 在左半边
    return -1  # 没找到

# ==========================================
# 2. 快速排序 (Quick Sort) - 面试手写版
# ==========================================
# 适用场景：需要手写排序算法时
# 时间复杂度：O(N log N)
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]  # 选基准值
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ==========================================
# 3. BFS 广度优先搜索 (Breadth-First Search)
# ==========================================
# 适用场景：最短路径、层序遍历、腐烂橘子、最小步数
# 核心数据结构：队列 (deque)
from collections import deque

def bfs(grid, start_nodes):
    # start_nodes 是所有起点的列表，例如 [(0,0), (0,1)]
    queue = deque(start_nodes)
    visited = set(start_nodes) # 记录访问过的节点，防止走回头路
    step = 0 # 记录层数/步数/时间
    
    while queue:
        size = len(queue) # 锁定当前层的节点数
        for _ in range(size):
            curr = queue.popleft()
            # if curr == target: return step  # 如果找到了目标
            
            # 遍历邻居 (上下左右)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = curr[0] + dx, curr[1] + dy
                
                # 检查边界 和 是否访问过
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        step += 1
    return -1

# ==========================================
# 4. DFS 回溯 (Backtracking)
# ==========================================
# 适用场景：全排列、组合、子集、所有路径
# 核心思想：做选择 -> 递归 -> 撤销选择
def backtrack_template(nums):
    res = []
    
    def backtrack(path, used):
        # 1. 结束条件
        if len(path) == len(nums):
            res.append(path[:]) # ⚠️ 必须拷贝
            return
        
        for i in range(len(nums)):
            # 剪枝：如果已经用过，跳过
            if used[i]: 
                continue
            
            # 2. 做选择
            path.append(nums[i])
            used[i] = True
            
            # 3. 进入下一层
            backtrack(path, used)
            
            # 4. 撤销选择 (回溯)
            path.pop()
            used[i] = False
            
    backtrack([], [False] * len(nums))
    return res

# ==========================================
# 5. 链表反转 (Reverse Linked List)
# ==========================================
# 适用场景：反转链表、回文链表、K个一组反转
# 核心思想：双指针 (prev, curr)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next # 1. 暂存后继节点
        curr.next = prev      # 2. 修改引用指向前驱
        prev = curr           # 3. prev 前移
        curr = next_node      # 4. curr 前移
    return prev # prev 最终指向新的头节点
