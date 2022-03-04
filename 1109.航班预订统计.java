/*
 * @lc app=leetcode.cn id=1109 lang=java
 *
 * [1109] 航班预订统计
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

    public int[] result() {
        int[] ret = new int[diff.length];
        ret[0] = diff[0];
        for (int i = 1; i < diff.length; i++) {
            ret[i] = ret[i - 1] + diff[i];
        }
        return ret;
    }

}

class Solution {

    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] nums = new int[n];
        Difference df = new Difference(nums);
        for (int[] booking : bookings) {
            int i = booking[0] - 1;
            int j = booking[1] - 1;
            int val = booking[2];
            df.increment(i, j, val);
        }
        return df.result();
    }
}
// @lc code=end
