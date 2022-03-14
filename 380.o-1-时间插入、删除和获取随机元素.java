import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

/*
 * @lc app=leetcode.cn id=380 lang=java
 *
 * [380] O(1) 时间插入、删除和获取随机元素
 */

// @lc code=start
class RandomizedSet {

    List<Integer> nums;
    HashMap<Integer, Integer> val2Index;
    Random random = new Random();

    public RandomizedSet() {
        nums = new ArrayList<>();
        val2Index = new HashMap<>();
    }

    public boolean insert(int val) {
        if (val2Index.containsKey(val)) {
            return false;
        }
        val2Index.put(val, nums.size());
        nums.add(nums.size(), val);
        return true;
    }

    public boolean remove(int val) {
        if (!val2Index.containsKey(val)) {
            return false;
        }
        // 获取索引
        int index = val2Index.get(val);
        int last = nums.get(nums.size() - 1);
        // 交换值
        nums.set(index, last);
        val2Index.put(last, index);
        val2Index.remove(val);
        nums.remove(nums.size() - 1);
        return true;
    }

    public int getRandom() {
        return nums.get(random.nextInt(nums.size()));
    }

    public static void main(String[] args) {
        RandomizedSet rs = new RandomizedSet();
        rs.insert(1);
        System.out.println(rs.getRandom());
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end
