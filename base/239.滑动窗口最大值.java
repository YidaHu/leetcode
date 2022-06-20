import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

import javafx.geometry.Side;

/*
 * @lc app=leetcode.cn id=239 lang=java
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> max = new ArrayList<>();
        ArrayDeque<Integer> indexDeque = new ArrayDeque<>();
        for (int i = 0; i < k - 1; i++) {
            while (!indexDeque.isEmpty() && nums[i] > nums[indexDeque.getLast()]) {
                indexDeque.removeLast();
            }
            indexDeque.addLast(i);
        }
        for (int i = k - 1; i < nums.length; i++) {
            // 先移除结尾较小的数据，保持队首为最大值
            while (!indexDeque.isEmpty() && nums[i] > nums[indexDeque.getLast()]) {
                indexDeque.removeLast();
            }
            // 移除队列中超出窗口的数据
            while (!indexDeque.isEmpty() && (i - indexDeque.getFirst()) >= k) {
                indexDeque.removeFirst();
            }
            // 当前添加到最后
            indexDeque.addLast(i);
            // 取出队首作为最大值
            max.add(nums[indexDeque.getFirst()]);
        }
        int[] res = max.stream().mapToInt(Integer::valueOf).toArray();
        return res;
    }
}
// @lc code=end
