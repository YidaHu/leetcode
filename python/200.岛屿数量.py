#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        
        # DFS 辅助函数：用于遍历并“淹没”一个岛屿
        def dfs(r, c):
            # 1. 递归终止条件（边界检查）：
            # - r < 0 or r >= row: 越过上下边界
            # - c < 0 or c >= col: 越过左右边界
            # - grid[r][c] == '0': 遇到水或者已经访问过的陆地
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            
            # 2. 标记当前格子为已访问（沉岛策略）
            # 将 '1' (陆地) 修改为 '0' (水)，避免后续重复访问
            grid[r][c] = '0'
            
            # 3. 递归访问上下左右四个相邻节点
            dfs(r - 1, c) # 上
            dfs(r + 1, c) # 下
            dfs(r, c - 1) # 左
            dfs(r, c + 1) # 右
            
            return

        # 遍历整个网格
        for r in range(row):
            for c in range(col):
                # 只有遇到 '1' (陆地) 时，才开始计算一个新的岛屿
                if grid[r][c] == '1':
                    # 发现新岛屿，计数 +1
                    count += 1
                    
                    # 使用 DFS 将当前岛屿的所有陆地都“推平”（置为 '0'）
                    # 这样主循环后续遍历到这个岛屿的其他部分时，会认为是水，跳过
                    dfs(r, c)
        
        return count


# @lc code=end

grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
print(Solution().numIslands(grid))
