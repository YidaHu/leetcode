#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))  # 返回 True
print(obj.search('app'))  # 返回 False
print(obj.startsWith('app'))  # 返回 True
obj.insert('app')
print(obj.search('app'))  # 返回 True
