
# 解码方法
# 暴力递归，类似于爬楼梯
class Solution:
    def numDecodings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.numDecodings(n-1)+self.numDecodings(n-2)


nums = "22645"
s = Solution()
s.numDecodings(len(nums))

# 解码方法
# 动态规划


class Solution1:
    def numDecodings(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


nums = "22645"
s = Solution1()
s.numDecodings(len(nums))
