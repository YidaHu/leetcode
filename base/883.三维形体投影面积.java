/*
 * @lc app=leetcode.cn id=883 lang=java
 *
 * [883] 三维形体投影面积
 */

// @lc code=start
class Solution {
    public int projectionArea(int[][] grid) {
        int top = 0;
        int front = 0;
        int side = 0;
        int[] sideMax = new int[grid[0].length];
        for (int i = 0; i < sideMax.length; i++) {
            sideMax[i] = 0;
        }
        for (int i = 0; i < grid.length; i++) {
            int frontMax = 0;
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] > 0) {
                    top++;
                }
                if (grid[i][j] > frontMax) {
                    frontMax = grid[i][j];
                }
                if (sideMax[j] < grid[i][j]) {
                    sideMax[j] = grid[i][j];
                }
            }
            front += frontMax;
        }
        for (int i = 0; i < sideMax.length; i++) {
            side += sideMax[i];
        }
        return top + front + side;
    }
}
// @lc code=end

