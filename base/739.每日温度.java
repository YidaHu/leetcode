import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=739 lang=java
 *
 * [739] 每日温度
 */

// @lc code=start
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();
        // 倒序遍历
        for (int i = n - 1; i >= 0; i--) {
            // 如果栈不为空，栈顶数据小于当前数据，推出
            while (!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
                stack.pop();
            }
            // 栈为空时，没有下一个更大元素。否则，栈顶索引到当前索引的距离为值
            res[i] = stack.isEmpty() ? 0 : (stack.peek() - i);
            // 保存当前索引
            stack.push(i);
        }
        return res;
    }
}
// @lc code=end
