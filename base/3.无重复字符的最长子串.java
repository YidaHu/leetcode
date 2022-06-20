import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> window = new HashMap<>();
        int left = 0, right = 0;
        int res = 0;
        while (right < s.length()) {
            char r = s.charAt(right);
            right++;
            window.put(r, window.getOrDefault(r, 0) + 1);
            while (window.getOrDefault(r, 0) > 1) {
                char l = s.charAt(left);
                left++;
                window.put(l, window.get(l) - 1);
            }
            if (res < right - left) {
                res = right - left;
            }
        }
        return res;
    }
}
// @lc code=end
