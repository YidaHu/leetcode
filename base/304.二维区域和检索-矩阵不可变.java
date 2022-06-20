/*
 * @lc app=leetcode.cn id=304 lang=java
 *
 * [304] 二维区域和检索 - 矩阵不可变
 */

// @lc code=start
class NumMatrix {
    private int[][] preMatrix;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        if (m == 0 || n == 0)
            return;
        preMatrix = new int[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                // 区域A
                int aSum = preMatrix[i - 1][j];
                // 区域B
                int bSum = preMatrix[i][j - 1];
                // 重复区域
                int repeatRegion = preMatrix[i - 1][j - 1];
                preMatrix[i][j] = matrix[i - 1][j - 1] + aSum + bSum - repeatRegion;
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        // 区域A
        int aSum = preMatrix[row1][col2 + 1];
        // 区域B
        int bSum = preMatrix[row2 + 1][col1];
        // 重复区域
        int repeatRegion = preMatrix[row1][col1];
        return preMatrix[row2 + 1][col2 + 1] - aSum - bSum + repeatRegion;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
// @lc code=end
