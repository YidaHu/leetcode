#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 辅助栈，用来暂存"还没处理完"的数字和字符串
        stack = []

        # 当前正在构建的数字（倍数）
        current_num = 0
        # 当前正在构建的字符串
        current_str = ''

        for char in s:
            if char.isdigit():
                # 如果是数字，可能是多位数，所以要 *10 + int
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 遇到左括号，说明要开始处理一个新的子串了
                # 把之前的状态（倍数和字符串）压入栈中保存
                stack.append((current_str, current_num))
                # 重置当前状态，准备处理括号里面的内容
                current_str = ''
                current_num = 0
            elif char == ']':
                # 遇到右括号，说明当前的子串处理完了
                # 弹出栈顶元素：之前保存的字符串 prev_str 和 倍数 num
                prev_str, num = stack.pop()
                # 核心逻辑：新字符串 = 之前的字符串 + (当前括号里的字符串 * 倍数)
                current_str = prev_str + current_str * num
            else:
                # 如果是普通字符，直接拼接到当前字符串后面
                current_str += char

        return current_str


# @lc code=end
s = '3[a2[c]]'
print(Solution().decodeString(s))
