/*
 * @lc app=leetcode.cn id=806 lang=java
 *
 * [806] 写字符串需要的行数
 */

// @lc code=start
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int line = 1;
        int width = 0;
        for (char c : s.toCharArray()) {
            int need = widths[c - 97];
            width += need;
            if (width > 100) {
                line++;
                width = need;
            }
        }
        int[] result = new int[2];
        result[0] = line;
        result[1] = width;
        return result;
    }
}
// @lc code=end

