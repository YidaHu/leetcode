#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 获取两个数组的总长度
        m, n = len(nums1), len(nums2)
        total_len = m + n

        # 定义一个辅助函数：在两个有序数组中找到第 k 小的数
        # k 是从 1 开始计数的
        def getKthElement(k):
            index1, index2 = 0, 0
            
            while True:
                # 边界情况 1: nums1 已经全部排除完了，直接返回 nums2 中剩下的第 k 个
                if index1 == m:
                    return nums2[index2 + k - 1]
                # 边界情况 2: nums2 已经全部排除完了，直接返回 nums1 中剩下的第 k 个
                if index2 == n:
                    return nums1[index1 + k - 1]
                # 边界情况 3: k 减小到 1 了，说明我们要找的就是当前两个数组起点的最小值
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况: 比较两个数组 k/2 位置的值
                # 我们尝试排除 k/2 个元素，但是要防止索引越界
                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                
                pivot1 = nums1[new_index1]
                pivot2 = nums2[new_index2]

                if pivot1 <= pivot2:
                    # nums1 的前半部分 (从 index1 到 new_index1) 肯定不是第 k 大，可以安全排除
                    # 排除的数量是 count = new_index1 - index1 + 1
                    k -= (new_index1 - index1 + 1)
                    index1 = new_index1 + 1
                else:
                    # nums2 的前半部分可以排除
                    k -= (new_index2 - index2 + 1)
                    index2 = new_index2 + 1

        # 如果总长度是奇数，中位数就是第 (total_len + 1) / 2 小的数
        if total_len % 2 == 1:
            return float(getKthElement((total_len + 1) // 2))
        # 如果总长度是偶数，中位数是第 total_len / 2 和第 total_len / 2 + 1 小的数的平均值
        else:
            return (getKthElement(total_len // 2) + getKthElement(total_len // 2 + 1)) / 2.0
        
        
# @lc code=end

nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))