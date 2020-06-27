#全排列
#给定一个可包含重复数字的序列，返回所有不重复的全排列。
#在一定会产生重复结果集的地方剪枝。
#我们可以在搜索之前就对候选数组排序，一旦发现这一支搜索下去可能搜索到重复的元素就停止搜索，这样结果集中不会包含重复元素。
class Solution:
    def permuteUnique(self,nums:list):
        def dfs(nums,size,depth,path,used,res):
            if depth==size:
                tmp=[]
                tmp.extend(path)
                res.append(tmp)
                return res
            for i in range(size):
                if not used[i]:
                    if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                        continue
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,res)
                    used[i]=False
                    path.pop()
        size=len(nums)
        if size==0:
            return []
        res=[]
        used=[False for i in range(size)]
        dfs(nums,size,0,[],used,res)
        return res
if __name__ == '__main__':
    nums=[1,1,1,2]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)    
