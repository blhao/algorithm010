# 最小路径和
# 给定一个包含非负整数的M*N 网格，找出一条路线，从左上角到右下角，使得路径上的数字之和最小！
# 动态规划--不需要额外空间
# 自顶向下
# 实时改变当前位置（i，j）的值grid[i][j]，表示直到走到（i，j）的最小路径和
# 时间复杂度0(m*n) 空间复杂度0(1)
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution()
s.minPathSum(grid)


# 最小路径和
# 给定一个包含非负整数的M*N 网格，找出一条路线，从左上角到右下角，使得路径上的数字之和最小！
# 动态规划--需要额外空间
# 自顶向下
# 初始化一个二维数组：dp=[[0]*cols for i in range(rows)]
# dp[i][j]的值表示直到走到（i，j）的最小路径和
# 时间复杂度0(m*n) 空间复杂度0(m*n)
class Solution1:
    def minPathSum(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for i in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(rows):
            for j in range(cols):
                if i == j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[rows-1][cols-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution1()
s.minPathSum(grid)

# 最小路径和
# 自下向上
# dp[i][j]当前位置到右下角最小路径和


class Solution2:
    def minPathSum(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for i in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if (i == rows-1) and (j == cols-1):
                    continue
                elif i == rows-1:
                    dp[i][j] = dp[i][j+1]+grid[i][j]
                elif j == cols-1:
                    dp[i][j] = dp[i+1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1])+grid[i][j]
        return dp[0][0]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution2()
s.minPathSum(grid)
