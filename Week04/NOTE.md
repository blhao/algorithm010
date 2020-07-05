<h3>第四周学习笔记 </h3>
<h4>1、深度优先搜索：</h4>
<pre>代码模板：
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator # already visited
        return
    visited.add(node) # process current node here.
    ...
    for next_node in node.children():
       if next_node not in visited:
           dfs(next_node, visited)
</pre>
<h4>2、广度优先搜索：</h4>
<p><pre>代码模板：
def BFS(graph, start, end):
    visited = set()
    queue = []
    queue.append([start])
    while queue:
       node = queue.pop()
       visited.add(node)
       process(node)
       nodes = generate_related_nodes(node)
       queue.push(nodes) # other processing work
</pre></p>
<h4>3、贪心算法</h4>
<pre>
贪心算法一般按如下步骤进行：
①建立数学模型来描述问题  。
②把求解的问题分成若干个子问题
③对每个子问题求解，得到子问题的局部最优解
④把子问题的解局部最优解合成原来解问题的一个解
贪心算法是一种对某些求最优解问题的更简单、更迅速的设计技术。贪心算法的特点是一步一步地进行，常以当前情况为基础根据某个优化测度作最优选择，而不考虑各种可能的整体情况，省去了为找最优解要穷尽所有可能而必须耗费的大量时间。贪心算法采用自顶向下，以迭代的方法做出相继的贪心选择，每做一次贪心选择，就将所求问题简化为一个规模更小的子问题，通过每一步贪心选择，可得到问题的一个最优解。虽然每一步上都要保证能获得局部最优解，但由此产生的全局解有时不一定是最优的，所以贪心算法不要回溯
</pre>
<h4>4、二分查找</h4>
<pre>
'''
>>找到变化点，关于变化点的特点：
所有变化点左侧元素 > 数组第一个元素
所有变化点右侧元素 < 数组第一个元素
>>算法
1、找到数组的中间元素 mid。
2、如果中间元素 > 数组第一个元素，我们需要在 mid 右边搜索变化点。
3、如果中间元素 < 数组第一个元素，我们需要在 mid 做边搜索变化点。
4、当我们找到变化点时停止搜索，当以下条件满足任意一个即可：
nums[mid] > nums[mid + 1]，因此 mid+1 是最小值。
nums[mid - 1] > nums[mid]，因此 mid 是最小值。
'''
</pre>
<pre>代码模板：
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target: # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
</pre>
<h4>5、使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方</h4>
<pre>
class Solution:
    def findMin(self, nums: list) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums)-1
        if nums[end] > nums[start]:
            return nums[start]
        while start <= end:
            mid = start+(start+end)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[start]:
                start = mid+1
            else:
                end = mid-1
</pre>
