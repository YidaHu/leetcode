#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        ret = []

        while True:
            for i in range(l, r + 1):
                ret.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                ret.append(matrix[i][r])
            r -= 1
            if r < l:
                break

            for i in range(r, l - 1, -1):
                ret.append(matrix[b][i])
            b -= 1
            if b < t:
                break

            for i in range(b, t - 1, -1):
                ret.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return ret


# @lc code=end

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
