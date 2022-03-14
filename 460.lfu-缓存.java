import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;

/*
 * @lc app=leetcode.cn id=460 lang=java
 *
 * [460] LFU 缓存
 */

// @lc code=start
class LFUCache {

    int cap;
    int minFreq;
    LinkedHashMap<Integer, Integer> keyToVal;
    LinkedHashMap<Integer, Integer> keyToFreq;
    LinkedHashMap<Integer, LinkedHashSet<Integer>> freqToKeys;

    public LFUCache(int capacity) {
        this.cap = capacity;
        this.minFreq = 0;
        this.keyToVal = new LinkedHashMap<>();
        this.keyToFreq = new LinkedHashMap();
        this.freqToKeys = new LinkedHashMap();
    }

    public int get(int key) {
        if (!keyToVal.containsKey(key)) {
            return -1;
        }
        increaseFreq(key);
        return keyToVal.get(key);
    }

    public void put(int key, int value) {
        if (cap == 0) {
            return;
        }
        if (keyToVal.containsKey(key)) {
            increaseFreq(key);
            keyToVal.put(key, value);
            return;
        }
        if (keyToVal.size() >= cap) {
            removeMinFreq();
        }
        keyToVal.put(key, value);
        keyToFreq.put(key, 1);
        freqToKeys.putIfAbsent(1, new LinkedHashSet<>());
        freqToKeys.get(1).add(key);
        this.minFreq = 1;
    }

    public void increaseFreq(int key) {
        int freq = keyToFreq.get(key);
        keyToFreq.put(key, freq + 1);
        freqToKeys.putIfAbsent(freq + 1, new LinkedHashSet<>());
        freqToKeys.get(freq + 1).add(key);
        freqToKeys.get(freq).remove(key);
        if (freqToKeys.get(freq).size() == 0) {
            freqToKeys.remove(freq);
            if (freq == this.minFreq) {
                this.minFreq++;
            }
        }

    }

    public void removeMinFreq() {
        int oldKey = freqToKeys.get(this.minFreq).iterator().next();
        keyToVal.remove(oldKey);
        keyToFreq.remove(oldKey);
        freqToKeys.get(this.minFreq).remove(oldKey);
        if (freqToKeys.get(this.minFreq).size() == 0) {
            freqToKeys.remove(this.minFreq);
        }
    }

}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end
