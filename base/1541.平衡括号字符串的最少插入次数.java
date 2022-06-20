/*
 * @lc app=leetcode.cn id=1541 lang=java
 *
 * [1541] 平衡括号字符串的最少插入次数
 */

// @lc code=start
class Solution {
    public int minInsertions(String s) {
        int res = 0;
        int need = 0;
        char[] chars = s.toCharArray();
        if (chars.length == 0) {
            return 0;
        }
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') {
                need += 2;
                if (need % 2 == 1) {
                    need--;
                    res++;
                }
            }
            if (chars[i] == ')') {
                need--;
                if (need == -1) {
                    need = 1;
                    res++;
                }
            }
        }
        return res + need;
    }
}
// @lc code=end
