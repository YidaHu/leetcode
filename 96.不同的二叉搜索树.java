import java.util.Map;

/*
 * @lc app=leetcode.cn id=96 lang=java
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    public int numTrees(int n) {
        if (n <= 1) {
            return 1;
        }
        // 已经有n的缓存，直接返回
        if (map.containsKey(n)) {
            return map.get(n);
        }
        int sum = 0;
        // 遍历n，每个都可做根
        for (int i = 1; i <=n ; i++) {
            // 左右子树笛卡尔积
            sum += numTrees(i - 1) * numTrees(n - i);
        }
        // 缓存n的不同次数，减少后面计算量
        map.put(n, sum);
        return sum;
    }
}
// @lc code=end

