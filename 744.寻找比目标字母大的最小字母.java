/*
 * @lc app=leetcode.cn id=744 lang=java
 *
 * [744] 寻找比目标字母大的最小字母
 */

// @lc code=start
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char ret = letters[0];
        for (char c: letters) {
            if (c > target) {
                return c;
            }
        }
        return ret;
    }
}
// @lc code=end

