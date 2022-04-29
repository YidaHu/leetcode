import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=908 lang=java
 *
 * [908] 最小差值 I
 */

// @lc code=start
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int min = Arrays.stream(nums).min().getAsInt();
        int max = Arrays.stream(nums).max().getAsInt();
        int res = max - min;
        if (res == 0) {
            return 0;
        }
        if (res <= k * 2) {
            return 0;
        }
        return res - k * 2;
    }
}
// @lc code=end

