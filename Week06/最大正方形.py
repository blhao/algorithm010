
# 最大正方形
# 暴力法
# 遍历矩阵中的每个元素，遇到1，则作为正方形的左上角
# 根据左上角，计算可能的最大正方形的边长（不超出矩阵的行数和列数）
# 每次在下方新增一行，以及在右边新增一列，判断新增的行和列是否满足需要，值都是1
class Solution:
    def maxSquare(self, matrix: list) -> int:
        if not matrix:
            return 0
        maxSide = 0
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    maxSide = max(maxSide, 1)
                    currentMaxSide = min(rows-i, cols-j)
                    for k in range(1, currentMaxSide):
                        flag = True
                        if matrix[i+k][j+k] == 0:
                            break
                        for m in range(k):
                            if matrix[i+k][j+m] == 0 or matrix[i+m][j+k] == 0:
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k+1)
                        else:
                            break
        maxSquare = maxSide*maxSide
        return maxSquare


matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 1, 1]]
s = Solution()
s.maxSquare(matrix)


# 最大正方形
# 动态规划
# dp[i][j]表示以(i,j)为右下角，且只包含1的正方形的边长最大值
# 计算出所有的dp元素值，其中最大的值就是我们需要的
class Solution1:
    def maxSquare(self, matrix: list) -> int:
        if not matrix:
            return 0
        maxSize = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                maxSize = max(maxSize, dp[i][j])
        maxSquare = maxSize*maxSize
        return maxSquare


matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
s = Solution1()
s.maxSquare(matrix)
