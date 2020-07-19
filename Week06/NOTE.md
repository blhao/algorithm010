<h2>学习笔记</h2>
<h3>1、递归代码模板</h3>
<pre>
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
</pre>
<h3>2、分支代码模板</h3>
<pre>
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return

prepare data

data = prepare_data(problem)
subproblems = split_problem(problem, data)

conquer subproblems

subresult1 = self.divide_conquer(subproblems[0], p1, ...)
subresult2 = self.divide_conquer(subproblems[1], p1, ...)
subresult3 = self.divide_conquer(subproblems[2], p1, ...)
…

process and generate the final result

result = process_result(subresult1, subresult2, subresult3, …)

revert the current level states

</pre>
<h3>动态规划</h3>
<pre>
动态规划算法通常用于求解具有某种最优性质的问题。在这类问题中，可能会有许多可行解。每一个解都对应于一个值，我们希望找到具有最优值的解。动态规划算法与分治法类似，其基本思想也是将待求解问题分解成若干个子问题，先求解子问题，然后从这些子问题的解得到原问题的解。与分治法不同的是，适合于用动态规划求解的问题，经分解得到子问题往往不是互相独立的。若用分治法来解这类问题，则分解得到的子问题数目太多，有些子问题被重复计算了很多次。如果我们能够保存已解决的子问题的答案，而在需要时再找出已求得的答案，这样就可以避免大量的重复计算，节省时间。我们可以用一个表来记录所有已解的子问题的答案。不管该子问题以后是否被用到，只要它被计算过，就将其结果填入表中。这就是动态规划法的基本思路。具体的动态规划算法多种多样，但它们具有相同的填表格式.
</pre>
<pre>
买麦股篇的最佳时期
动态规划
只能买卖一次
dp[i][0]表示今天手里没有股票，dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
dp[i][1]表示今天手里有股票，dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
class Solution:
    def maxProfit(self,prices:list):
        if not prices:
            return 0
        size=len(prices)
        if size ==1:
            return 0
        dp = [[0]*2 for i in range(size)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,size):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[size-1][0]
prices=[7,1,5,3,6,4]
s=Solution()
s.maxProfit(prices)
</pre>
<pre>
打家劫舍
生成一个二维数组dp[i][0]表示i号房不偷时，偷到的最大金额；dp[i][1]表示i号房偷，偷到的最大金额
class Solution:
    def rob(self,nums:list):
        if not nums:
            return 0
        size=len(nums)
        if size==1:
            return nums[0]
        dp=[[0]*2 for i in range(size)]
        dp[0][0]=0
        dp[0][1]=nums[0]
        for i in range(1,size):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=dp[i-1][0]+nums[i]
        return max(dp[size-1][0],dp[size-1][1])
#nums=[2,7,9,3,1]
nums=[1,2,3,1]
s=Solution()
s.rob(nums)
</pre>
<pre>
爬楼梯
coin change: 有三种硬币 1，2，5，问得到11，最少用几枚硬币？
每次可以走1步，或者2步，或者5步，走到11级台接，最少走几步？
class Solution:
    def climbStairs(self,n:list):
        dp=[0 for i in range(n+1)]
        for i in range(1,n+1):
            if i<=2 or i==5:
                dp[i]=1
            elif 2<i<5:
                dp[i]=min(dp[i-1],dp[i-2])+1
            else:
                dp[i]=min(dp[i-1],dp[i-2],dp[i-5])+1
        return dp[n]
s=Solution()
s.climbStairs(11)

</pre>
