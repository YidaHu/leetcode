import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=567 lang=java
 *
 * [567] 字符串的排列
 */

// @lc code=start
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        for (char c : s1.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }
        int valid = 0;
        int left = 0, right = 0;
        while (right < s2.length()) {
            char r = s2.charAt(right);
            right++;
            // 数据更新
            if (need.containsKey(r)) {
                window.put(r, window.getOrDefault(r, 0) + 1);
                if (need.get(r).equals(window.get(r))) {
                    valid++;
                }
            }
            // 窗口缩小时机，就是满足条件时窗口长度大于子串长度
            while (right - left >= s1.length()) {
                // 如果大小一样，说明排列一样
                if (valid == need.size()) {
                    return true;
                }
                char l = s2.charAt(left);
                left++;
                if (need.containsKey(l)) {
                    if (need.get(l).equals(window.get(l))) {
                        valid--;
                    }
                    window.put(l, window.get(l) - 1);
                }
            }
        }
        return false;
    }
}
// @lc code=end
