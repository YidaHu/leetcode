import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Random;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=710 lang=java
 *
 * [710] 黑名单中的随机数
 */

// @lc code=start
class Solution {

    Random rd = new Random();
    HashMap<Integer, Integer> map;
    int wl;

    public Solution(int n, int[] blacklist) {
        map = new HashMap<>();
        // 白名单个数
        wl = n - blacklist.length;
        // 可以将[0,N)看做为一个数组，随机0到wL的数字即可，
        // 因为0到wL中间可能存在黑名单，所以可以将0到wL中黑名单的数字，
        // 映射到wL到N-1里边的白名单数字
        Set<Integer> set = new HashSet<>();
        // ①拿到所有比wL大的数字集合
        for (int i = wl; i < n; i++) {
            set.add(i);
        }
        // ②去掉数字集合中的黑名单数字，只留下白名单数字，供映射使用
        for (int num : blacklist) {
            set.remove(num);
        }
        // ③映射，将小于wL的黑名单全部映射到大于wL的白名单中
        Iterator<Integer> it = set.iterator();
        for (int num : blacklist) {
            if (num < wl) {
                map.put(num, it.next());
            }
        }

    }

    public int pick() {
        // 如果命中黑名单，取映射值。否则直接返回
        int index = rd.nextInt(wl);
        return map.getOrDefault(index, index);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.pick();
 */
// @lc code=end
