#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # 动态规划：直接在原数组 grid 上修改，节省空间
        # grid[i][j] 代表从 (0,0) 走到 (i,j) 的最小路径和
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    # 第一行只能从左边走过来
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    # 第一列只能从上边走过来
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    # 其他位置，取左边和上边的较小值 + 当前值
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
        return grid[rows - 1][cols - 1]
        
        
        
        
        
# @lc code=end

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))