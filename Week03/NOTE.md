学习笔记
1、第三周学习了分治和回溯的实现和特性
分治和回溯的本质其实就是寻找重复性以及分解问题，最后再组合子问题的结果。
2、分支代码模板：

# Python

def divide_conquer(problem, param1, param2, ...):

# recursion terminator

if problem is None:
print_result
return

# prepare data

data = prepare_data(problem)
subproblems = split_problem(problem, data)

# conquer subproblems

subresult1 = self.divide_conquer(subproblems[0], p1, ...)
subresult2 = self.divide_conquer(subproblems[1], p1, ...)
subresult3 = self.divide_conquer(subproblems[2], p1, ...)
…

# process and generate the final result

result = process_result(subresult1, subresult2, subresult3, …)

# revert the current level states

3、通过分析“括号生成”算法，掌握分治回溯原理
方法 1：做减法
1）当左右括号都有大于 0 个可以使用的时候，才产生分支；
2）产生左分支，只看是否还有左括号可以使用；
3）产生右分支，要收到左分支影响，可使用的右括号一定要大于可以使用的左括号数量；
4）左右括号都剩余 0 个时结束；

if left==0 and right==0:
&nbsp;&nbsp;res.append(cur_str)
&nbsp;&nbsp;return
if right<left:
&nbsp;&nbsp;return
if left>0:
&nbsp;&nbsp;dfs(cur_str+'(',left-1,right)
if right>0:
&nbsp;&nbsp;dfs(cur_str+')',left,right-1)

方法 2、做加法：
1、left 和 right 表示已经使用了几个；
2、当 left 和 right 都等于 n 时，结束；
3、left < right 剪掉

if left==n and right==n:
&nbsp;&nbsp;res.append(cur_str)
&nbsp;&nbsp;return
if left<right:
&nbsp;&nbsp;return
if left<n:
&nbsp;&nbsp;dfs(cur_str+'(',left+1,right,n)
if right<n:
&nbsp;&nbsp;dfs(cur_str+')',left,right+1,n)
