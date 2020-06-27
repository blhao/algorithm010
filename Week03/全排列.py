#全排列一
#创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同： 
#返回p中任意取r个元素做排列的元组的迭代器。
#r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度。
#combinations(nums,r)  combinations_with_replacement(nums,r)  组合函数
from itertools import permutations
nums=[1,2,3]
res = list(permutations(nums,2))
print(res)

#全排列二
class Solution:
    def permute(self,nums:list):
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first,n):
                #动态维护数组
                nums[first],nums[i]=nums[i],nums[first]
                #继续递归填写下一个数
                backtrack(first+1)
                #插销操作
                nums[first],nums[i]=nums[i],nums[first]
        n = len(nums)
        res=[]
        backtrack(0)
        return res
nums=[1,2,3,4]
X=Solution()
print(X.permute(nums))


#全排列三
#设置两个状态变量：path：已经选了哪些数，到叶子结点时候，这些已经选择的数就构成了一个全排列；
#used：一个布尔数组 used，初始化的时候都为 false 表示这些数还没有被选择，当我们选定一个数的时候，就将这个数组的相应位置设置为 true ，
#这样在考虑下一个位置的时候，就能够以 O(1)的时间复杂度判断这个数是否被选择过，这是一种“以空间换时间”的思想。
#状态重置：在回到上一层结点的过程中，需要撤销上一次选择；
class Solution():
    def permute(self,nums:list):
        def dfs(nums,size,depth,path,used,res):
            if depth == size:
                tmp=[]
                tmp.extend(path)
                res.append(tmp)
                return
            for i in range(size):
                if not used[i]:
                    #设置状态变量
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,res)
                    #状态重置
                    used[i]=False
                    path.pop()
        size=len(nums)
        if size==0:
            return []
        used=[False for i in range(size)]
        res = []
        dfs(nums,size,0,[],used,res)
        return res
if __name__ == '__main__':
    nums=[1,2,3,4]
    solution = Solution()
    res = solution.permute(nums)
    print(res)


