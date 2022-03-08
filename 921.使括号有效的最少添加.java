/*
 * @lc app=leetcode.cn id=921 lang=java
 *
 * [921] 使括号有效的最少添加
 */

// @lc code=start
class Solution {
    public int minAddToMakeValid(String s) {
        int res = 0;
        int need = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') {
                need++;
            }
            if (chars[i] == ')') {
                need--;
                if (need == -1) {
                    need = 0;
                    res++;
                }
            }
        }
        return res + need;
    }
}
// @lc code=end
