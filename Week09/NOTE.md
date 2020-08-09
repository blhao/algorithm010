<pre>
不同路径2思路
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        #新建矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*width for i in range(height)]

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if not obstacleGrid[m][n]: #如果这一格没有障碍物
                    if m == n == 0:
                        dp[m][n] = 1
                     else:
                        a = dp[m-1][n] if m!=0 else 0 #上方格子
                        b = dp[m][n-1] if n!=0 else 0 #左方格子
                        dp[m][n] = a+b
        return dp[-1][-1]
</pre>
