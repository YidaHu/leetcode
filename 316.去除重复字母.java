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
        // 存储字符出现次数，考虑空间可以用字符数组char[]
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        ArrayDeque<Character> deque = new ArrayDeque<>();
        // 遍历
        for (char c : s.toCharArray()) {
            // 单调栈方式，分析最后一个是否比当前值大，并且尾值后面出现次数依然大于1，当前值在队列前未被使用
            while (!deque.isEmpty() && c < deque.getLast() && map.get(deque.getLast()) > 1 && !deque.contains(c)) {
                // 满足，减引用次数，删除值
                map.put(deque.getLast(), map.get(deque.getLast()) - 1);
                deque.removeLast();
            }
            // 队列未包含值，添加。否则删除一次引用
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
