import java.util.HashMap;


/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        for (char ch : t.toCharArray()) {
            need.put(ch, need.getOrDefault(ch, 0) + 1);
        }
        int left = 0, right = 0;
        int valid = 0;
        // 记录最小覆盖子串的起始索引和长度
        int start = 0, len = Integer.MAX_VALUE;
        while (right < s.length()) {
            // 即将移入窗口的字符
            char a = s.charAt(right);
            // 右移窗口
            right++;
            // 进行窗口内数据的一系列更新
            if (need.containsKey(a)) {
                window.put(a, window.getOrDefault(a, 0) + 1);
                if (window.get(a).equals(need.get(a))) {
                    valid++;
                }
            }
            // 判断左侧窗口是否要收缩
            while (valid == need.size()) {
                // 在这里更新最小覆盖子串
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                // 即将移出窗口的字符
                char b = s.charAt(left);
                // 左移窗口
                left++;
                // 进行窗口内数据的一系列更新
                if (need.containsKey(b)) {
                    if (need.get(b).equals(window.get(b))) {
                        valid--;
                    }
                    window.put(b, window.getOrDefault(b, 0) - 1);
                }

            }
        }
        // 返回最小覆盖子串
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);
    }

}
// @lc code=end
