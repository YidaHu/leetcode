import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为 K 的子数组
 * 前缀和主要适用场景，原始数组不被修改的情况下，频繁查询某个区间的累加和
 */

// @lc code=start
class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        // 用hash表，记录前缀和的同时记录前缀和出线的次数
        HashMap<Integer, Integer> map = new HashMap<>();
        int ret = 0;
        map.put(0, 1);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            int sumT = sum - k;
            if (map.containsKey(sumT)) {
                ret += map.get(sumT);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return ret;
    }
}
// @lc code=end
