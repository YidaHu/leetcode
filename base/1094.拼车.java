/*
 * @lc app=leetcode.cn id=1094 lang=java
 *
 * [1094] 拼车
 */

// @lc code=start

class Difference {
    private int[] diff;

    public Difference(int[] nums) {
        assert nums.length > 0;
        diff = new int[nums.length];
        diff[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            diff[i] = nums[i] - nums[i - 1];
        }
    }

    public void increment(int i, int j, int val) {
        diff[i] += val;
        if (j < diff.length - 1) {
            diff[j + 1] -= val;
        }
    }

    public boolean canCarry(int capacity) {
        int[] ret = new int[diff.length];
        ret[0] = diff[0];
        if (diff[0] > capacity) {
            return false;
        }
        for (int i = 1; i < diff.length; i++) {
            ret[i] = ret[i - 1] + diff[i];
            if (ret[i] > capacity) {
                return false;
            }
        }
        return true;
    }

}

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int maxLocation = 0;
        for (int[] trip : trips) {
            if (trip[2] > maxLocation) {
                maxLocation = trip[2];
            }
        }
        int[] nums = new int[maxLocation];
        Difference df = new Difference(nums);
        for (int[] trip : trips) {
            int i = trip[1];
            int j = trip[2] - 1;
            int val = trip[0];
            df.increment(i, j, val);
        }
        return df.canCarry(capacity);
    }
}
// @lc code=end
