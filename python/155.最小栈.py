#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # 核心逻辑修正：
        # 1. 如果 min_stack 为空，直接放入
        # 2. 如果新来的值 <= 当前最小值，也要放入 min_stack
        # 注意：不要清空 min_stack！我们需要保留"之前的最小值"作为历史记录
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
        

    def pop(self):
        """
        :rtype: None
        """
        # 弹出主栈栈顶
        val = self.stack.pop()
        # 如果弹出的值等于当前最小值，说明这个最小值被移除了
        # 此时 min_stack 也要弹出，露出"次小值"
        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # top 只是查看，不能 pop！
        # stack[-1] 获取栈顶元素
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # 直接返回 min_stack 栈顶，这就是当前的最小值
        if self.min_stack:
            return self.min_stack[-1]
        if self.min_stack:
            return self.min_stack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
obj = MinStack()
obj.push(0)
obj.push(3)
obj.push(1)
obj.pop()
print(obj.getMin())  # 返回 -3
obj.pop()
print(obj.top())     # 返回 0
print(obj.getMin())  # 返回 -2
