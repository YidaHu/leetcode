#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        【小白入门解析】最大子数组和

        这道题的核心是：如何判断一个子数组是“有潜力”的？

        想象你在玩一个累积财富的游戏，数组里的数字代表每天的收益（正数是赚钱，负数是亏钱）。
        你需要找出一个连续的时间段，让你赚的钱最多。

        【核心思路：贪心 / 动态规划】
        我们遍历每一天，思考一个问题：
        “我应该把今天的收益加入之前的累积中，还是抛弃过去的包袱，从今天重新开始？”

        决策逻辑：
        1. 如果之前的累积收益（pre_sum）是正数（>0）：
           说明之前的积累对我有帮助，那我就加上今天的钱。
           （比如之前赚了 10 块，今天亏 2 块，加起来还有 8 块，比单独今天的 -2 块要好）

        2. 如果之前的累积收益是负数（<=0）：
           说明之前的积累是个“拖油瓶”，只会拉低我今天的水平。
           那我就果断抛弃过去，从今天开始重新计算累积。
           （比如之前亏了 100 块，今天赚 5 块，如果加上之前的，我就还亏 95 块；不如直接从今天算，我就是赚 5 块）

        【算法步骤】：
        1. 准备一个变量 `current_sum` 记录当前的累积收益。
        2. 准备一个变量 `max_sum` 记录历史出现过的最大收益。
        3. 遍历数组中的每一个数字 `num`：
           - 如果 `current_sum > 0`，则 `current_sum += num`（继续积累）。
           - 否则，`current_sum = num`（重新开始）。
           - 每次变动后，都检查一下 `current_sum` 是否打破了历史记录 `max_sum`。
        """
        # 1. 初始化
        # max_sum 初始化为数组第一个元素（因为子数组至少包含一个元素）
        # current_sum 也初始化为第一个元素，表示以当前元素结尾的最大子数组和
        max_sum = nums[0]
        current_sum = nums[0]

        # 2. 从第二个元素开始遍历数组
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 3. 核心决策：继承还是重启？
            # 如果之前的累积和 (current_sum) 是正数，说明它对后续有贡献，我们选择“继承”，加上当前数字。
            if current_sum > 0:
                current_sum += num
            # 如果之前的累积和是负数或零，说明它会拖累当前数字，我们选择“重启”，直接从当前数字开始算。
            else:
                current_sum = num
            
            # 4. 更新历史最大值
            # 每次计算完新的 current_sum 后，都跟历史最大值 max_sum 比一下，保留最大的那个。
            max_sum = max(max_sum, current_sum)
            
        return max_sum


# @lc code=end

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
