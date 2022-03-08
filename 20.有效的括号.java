import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {

    // /**
    // * 1.暴力破解
    // * @param s
    // * @return
    // */
    // public boolean isValid(String s) {
    // Map<String, String> map = new HashMap<>();
    // map.put(")", "(");
    // map.put("}", "{");
    // map.put("]", "[");
    // Stack<String> stack = new Stack<>();
    // for (char c : s.toCharArray()) {
    // String str = String.valueOf(c);
    // if (map.containsKey(str) && stack.isEmpty()) {
    // return false;
    // }
    // if (!map.containsKey(str)) {
    // stack.push(str);
    // } else {
    // if (!map.get(str).equals(stack.pop())) {
    // return false;
    // }
    // }
    // }
    // if (stack.isEmpty()) {
    // return true;
    // }
    // return false;
    // }

    public boolean isValid(String s) {
        List<Character> ch = new ArrayList<>();
        ch.add(']');
        ch.add('}');
        ch.add(')');
        char[] chars = s.toCharArray();
        int n = chars.length;
        int left = 0, right = chars.length - 1;
        while (left != right) {
            if (chars[left] != chars[right]) {
                return false;
            }
            if (ch.contains(chars[left])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
// @lc code=end
