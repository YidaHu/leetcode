from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        计算最长连续序列的长度。
        算法思路：
        1. 使用哈希集合（set）存储数组元素，实现 O(1) 的查找时间复杂度，并去重。
        2. 遍历集合中的每个元素，判断其是否为某个连续序列的起点。
           - 如果 num - 1 不在集合中，说明 num 是一个新序列的起点。
        3. 从起点开始，不断尝试匹配 num + 1, num + 2... 直到断开。
        4. 记录并更新最长序列的长度。
        """
        long_count = 0
        # 处理空数组的情况
        if not nums:
            return 0
        
        # 将列表转换为集合，去重并提高查找效率
        nums = set(nums)
        
        for num in nums:
            # 只有当 num - 1 不在集合中时，num 才是一个连续序列的起点
            # 这样可以避免重复计算同一个序列的一部分
            if num - 1 not in nums:
                current_count = 1
                current_num = num
                
                # 从起点开始向后寻找连续的数字
                while current_num + 1 in nums:
                    current_count += 1
                    current_num += 1
                
                # 更新全局最长连续序列长度
                long_count = max(current_count, long_count)
                
        return long_count


nums = [4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]
print(Solution().longestConsecutive(nums))
