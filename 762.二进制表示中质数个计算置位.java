/*
 * @lc app=leetcode.cn id=762 lang=java
 *
 * [762] 二进制表示中质数个计算置位
 */

// @lc code=start
class Solution {

    // 1.数学加位运算
    // public int countPrimeSetBits(int left, int right) {
    //     int res = 0;
    //     for (int i = left; i <= right; i++) {
    //         if (isPrime(Integer.bitCount(i))) {
    //             res++;
    //         }
    //     }
    //     return res;
    // }

    // 2. 判断质数优化
    public int countPrimeSetBits(int left, int right) {
        int res = 0;
        for (int i = left; i <= right; i++) {
            if (((1 << Integer.bitCount(i)) & 665772) != 0) {
                res++;
            }
        }
        return res;
    }

    public boolean isPrime(int x) {
        if (x < 2) {
            return false;
        }
        for (int i = 2; i * i <= x; ++i) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

