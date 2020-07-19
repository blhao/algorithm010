# 编辑距离
# 递归
# dp[i,j] 返回s1[0...i] and s2[0....j] 的最小编辑距离
class Solution:
    def minDistance(self, s1: str, s2: str):
        def dp(i, j):
            # base case
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if s1[i] == s2[j]:
                return dp(i-1, j-1)
            else:
                # 插入，删除，替换操作得到的距离中，取最小值
                return min(dp(i, j-1), dp(i-1, j), dp(i-1, j-1))+1
        # 初始化，指向最后一个字符
        return dp(len(s1)-1, len(s2)-1)


s1 = "horse"
s2 = "ros"
s = Solution()
s.minDistance(s1, s2)


# 编辑距离
# 动态规划
# dp[i][j]存储s1[0...i] and s2[0....j] 的最小编辑距离
class Solution1:
    def minDistance(self, s1: str, s2: str):
        if (not s1) or (not s2):
            return 0
        m = len(s1)
        n = len(s2)
        dp = [[0]*(n+1) for i in range(m+1)]
        # base case
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[m][n]


s1 = "horse"
s2 = "ros"
s = Solution1()
s.minDistance(s1, s2)
