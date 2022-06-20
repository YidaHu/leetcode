import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=496 lang=java
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<Integer>();
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] res = new int[nums1.length];
        for (int num : nums2) {
            // 遍历栈，记录数字和下一个更大元素的映射
            while (!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            // 更大元素入栈
            stack.push(num);
        }
        // 遍历获取
        for (int i = 0; i < nums1.length; i++) {
            // 如果存在，取值（最大元素），否则返回-1
            res[i] = map.getOrDefault(nums1[i], -1);
        }
        return res;
    }
}
// @lc code=end
