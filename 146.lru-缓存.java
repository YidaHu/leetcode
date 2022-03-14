import java.util.LinkedHashMap;

/*
 * @lc app=leetcode.cn id=146 lang=java
 *
 * [146] LRU 缓存
 */

// @lc code=start
class LRUCache {
    int capacity;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        // 不存在返回-1
        if (!cache.containsKey(key)) {
            return -1;
        }
        // 提升为最近使用
        makeRecently(key);
        return cache.get(key);
    }

    public void put(int key, int value) {
        // 包含键，提升为最近使用，赋值
        if (cache.containsKey(key)) {
            makeRecently(key);
            cache.put(key, value);
            return;
        }
        // 大于空间，淘汰最久使用键，然后赋新的键值
        if (cache.size() >= capacity) {
            int oldKey = cache.keySet().iterator().next();
            cache.remove(oldKey);
        }
        cache.put(key, value);
    }

    // 将数据提升为最近使用
    public void makeRecently(int key) {
        if (cache.containsKey(key)) {
            int val = cache.get(key);
            cache.remove(key);
            cache.put(key, val);
        }
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end
