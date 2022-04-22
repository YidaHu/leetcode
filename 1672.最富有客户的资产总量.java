/*
 * @lc app=leetcode.cn id=1672 lang=java
 *
 * [1672] 最富有客户的资产总量
 */

// @lc code=start
class Solution {
    public int maximumWealth(int[][] accounts) {
        int ret = 0;
        for (int i = 0; i < accounts.length; i++) {
            int sum = 0;
            for (int n : accounts[i]) {
                sum += n;
            }
            if (ret < sum) {
                ret = sum;
            }
        }
        return ret;
    }
}
// @lc code=end

