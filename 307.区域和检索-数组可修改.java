/*
 * @lc app=leetcode.cn id=307 lang=java
 *
 * [307] 区域和检索 - 数组可修改
 */

// @lc code=start
class NumArray {

    public int[] data;

    public NumArray(int[] nums) {
        this.data = nums;
    }
    
    public void update(int index, int val) {
        data[index] = val;
    }
    
    public int sumRange(int left, int right) {
        int sum = 0;
        while (left <= right) {
            sum += data[left];
            left++;
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
// @lc code=end

