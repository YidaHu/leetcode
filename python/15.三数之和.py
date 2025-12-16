#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. 排序：这是双指针法的前提
        nums.sort()
        res = []
        n = len(nums)
        
        # 2. 遍历第一个数 nums[i]
        for i in range(n - 2):
            # 优化1：如果最小的数都大于0，后面不可能凑出0了
            if nums[i] > 0:
                break
            
            # 优化2：去重（针对第一个数）
            # 如果当前数和前一个数一样，说明这种情况已经处理过了，跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 3. 双指针寻找另外两个数
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # 和太小，左指针右移让和变大
                    left += 1
                elif total > 0:
                    # 和太大，右指针左移让和变小
                    right -= 1
                else:
                    # 找到一组解
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 优化3：去重（针对第二、三个数）
                    # 必须先移动指针，再判断是否重复，或者先判断再移动
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # 找到答案后，两边都要收缩
                    left += 1
                    right -= 1
                    
        return res

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(s.threeSum([0,1,1])) # []
    print(s.threeSum([0,0,0])) # [[0,0,0]]
