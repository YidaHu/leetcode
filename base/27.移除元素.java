import java.util.Comparator;
import java.util.PriorityQueue;

import javax.lang.model.element.Element;

/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int left = 0, right = 0;
        while (right < n) {
            if (nums[right] != val) {
                nums[left] = nums[right];
                left++;
            }
            right++;
        }
        return left;
    }
}
// @lc code=end
