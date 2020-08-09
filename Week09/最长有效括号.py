# 最长有效括号
# 动态规划
# dp[i]表示以下标i为结尾的字符串最大有效括号
# if s[i]=')' and s[i-1]='(' dp[i]=dp[i-2]+2
# if s[i]=')' and s[i-1]=')'   if s[i-dp[i-1]-1]=='('  dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
class Solution:
    def longestValidParentheses(self, s: str):
        size = len(s)
        if size <= 1:
            return 0
        dp = [0]*size
        res = 0
        for i in range(size):
            if i > 0 and s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res


# s="(()"
s = ")()())"
r = Solution()
r.longestValidParentheses(s)
