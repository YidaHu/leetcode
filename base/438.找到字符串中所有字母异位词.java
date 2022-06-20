import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode.cn id=438 lang=java
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lc code=start
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        for (char c : p.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }
        int left = 0, right = 0;
        List<Integer> res = new ArrayList<>();
        int valid = 0;
        while (right < s.length()) {
            char r = s.charAt(right);
            right++;
            // 数据更新
            if (need.containsKey(r)) {
                window.put(r, window.getOrDefault(r, 0) + 1);
                if (need.get(r).equals(window.get(r))) {
                    valid++;
                }
            }
            while (valid == need.size()) {
                // 操作
                if (right - left == p.length()) {
                    res.add(left);
                }
                char l = s.charAt(left);
                left++;
                if (need.containsKey(l)) {
                    if (need.get(l).equals(window.get(l))) {
                        valid--;
                    }
                    window.put(l, window.get(l) - 1);
                }
            }
        }
        return res;

    }
}
// @lc code=end
