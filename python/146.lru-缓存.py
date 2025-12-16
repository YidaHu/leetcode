#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存
#

# @lc code=start
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cache.add(key, value)
        self.cache.move_to_end(key)
        
        if self.cache.keys > self.capacity:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))    # 返回 1
obj.put(3, 3)        # 该操作会使得密钥 2 作废
print(obj.get(2))    # 返回 -1 (未找到)
obj.put(4, 4)        # 该操作会使得密钥 1 作废
print(obj.get(1))    # 返回 -1 (未找到)
print(obj.get(3))    # 返回 3
print(obj.get(4))    # 返回 4
