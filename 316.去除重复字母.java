import java.util.ArrayDeque;
import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=316 lang=java
 *
 * [316] 去除重复字母
 */

// @lc code=start
class Solution {
    public static String removeDuplicateLetters(String s) {
        String res = "";
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        ArrayDeque<Character> deque = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            while (!deque.isEmpty() && c < deque.getLast() && map.get(deque.getLast()) > 1 && !deque.contains(c)) {
                map.put(deque.getLast(), map.get(deque.getLast()) - 1);
                deque.removeLast();
            }
            if (!deque.contains(c)) {
                deque.addLast(c);
            } else {
                map.put(c, map.get(c) - 1);
            }
        }
        for (Character c : deque) {
            res += c;
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(removeDuplicateLetters("bcabc"));
    }
}
// @lc code=end
