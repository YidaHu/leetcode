#
# @lc app=leetcode.cn id=994 lang=python
#
# [994] 腐烂的橘子
#

# @lc code=start
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 核心思路：多源 BFS (广度优先搜索)
        # 想象成病毒爆发，所有一开始烂的橘子同时向四周扩散
        
        row = len(grid)
        col = len(grid[0])
        
        # 使用 deque 优化队列操作，popleft() 是 O(1) 的
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # 1. 初始化：找出所有一开始就是烂的橘子，加入队列
        # 同时统计新鲜橘子的数量
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # 如果一开始就没有新鲜橘子，直接返回 0
        if fresh_count == 0:
            return 0
        
        # 2. BFS 循环
        while queue:
            size = len(queue)
            infected_this_round = False # 标记这一分钟是否有新橘子被感染
            
            # 遍历当前这一层的所有烂橘子
            for _ in range(size):
                r, c = queue.popleft()
                
                # 检查上下左右四个方向
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    
                    # 边界检查 + 必须是新鲜橘子
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        # 传染它！
                        grid[nr][nc] = 2 # 标记为烂，避免重复访问
                        fresh_count -= 1 # 新鲜橘子少一个
                        queue.append((nr, nc)) # 加入队列，下一分钟它会继续传染别人
                        infected_this_round = True
            
            # 只有这一轮真的传染了新橘子，时间才 +1
            if infected_this_round:
                minutes += 1
        
        # 3. 检查是否还有幸存者
        # 如果 fresh_count == 0，说明全部感染，返回时间
        # 否则说明有橘子被墙隔开了，永远烂不到，返回 -1
        return minutes if fresh_count == 0 else -1


# @lc code=end
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
