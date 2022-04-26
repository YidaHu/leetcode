import java.awt.List;
import java.util.Collection;
import java.util.Collections;
import java.util.Map;
import java.util.Random;

/*
 * @lc app=leetcode.cn id=398 lang=java
 *
 * [398] 随机数索引
 */

// @lc code=start
class Solution {

    Random rd = new Random();
    HashMap<Integer, List<Integer>> numMap = new LinkedHashMap<Integer, List<Integer>>();

    public Solution(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            List<Integer> list = numMap.getOrDefault(nums[i], new ArrayList<Integer>());
            list.add(i);
            numMap.put(nums[i], list);
        }
    }
    
    public int pick(int target) {
        List<Integer> list = this.numMap.getOrDefault(target, Collections.EMPTY_LIST);
        int len = list.size();
        int index = rd.nextInt(len);
        return list.get(index);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
// @lc code=end

