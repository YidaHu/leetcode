/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 0) return;
        if (nums.length == 1) return;
        int n = nums.length;
        int left = 0, right = 0;
        while (right < n) {
            if (nums[right] != 0) {
                nums[left] = nums[right];
                if (right > left) {
                    nums[right] = 0;
                }
                left++;
            }
            right++;
        }
    }
}
// @lc code=end

