# 最大有效括号
# 栈
# 遇到“）”出栈，遇到“（”进栈
# 有效括号的下标，放到一个数组中，排序以后，找到最长连续数列的长度就是最长有效括号长度！
class Solution:
    def longestValidParentheses(self, s: str):
        size = len(s)
        if size <= 1:
            return 0
        res = []
        stack = []
        for i in range(size):
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
            if s[i] == '(':
                stack.append(i)
        res.sort()
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n-1 and res[j+1] == res[j]+1:
                j += 1
            ans = max(ans, j-i+1)
            i = j+1
        return ans


s = "(()"
r = Solution()
r.longestValidParentheses(s)

# 最大有效括号
# 动态规划
# dp[i]表示以下标i为结尾的字符串最大有效括号
# if s[i]=')' and s[i-1]='(' dp[i]=dp[i-2]+2
# if s[i]=')' and s[i-1]=')'   if s[i-dp[i-1]-1]=='('  dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]


class Solution1:
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
r = Solution1()
r.longestValidParentheses(s)
