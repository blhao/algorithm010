#组合一
from itertools import combinations
def combine1(n:int,k:int):
    nums=list(range(1, n + 1))
    res = list(combinations(nums,k))
    return res
print(combine(4,2))

#组合二
#回溯法
#这是一个回溯法函数，它将第一个添加到组合中的数和现有的组合作为参数，backtrack(first, curr)
#若组合完成- 添加到输出中。
#遍历从 first t到 n的所有整数。
#将整数 i 添加到现有组合 curr中。
#继续向组合中添加更多整数 :
#backtrack(i + 1, curr).
#将 i 从 curr中移除，实现回溯。
def combine2(n:int,k:int):
    def backtrack(first=1,cur=[]):
        # if the combination is done
        if len(cur) == k:
            res.append(cur)
        for i in range(1,n+1):
            # add i into the current combination
            cur.append(i)
            # use next integers to complete the combination
            backtrack(first+1,cur)
            # backtrack
            cur.pop()
    res=[]
    backtrack(1,res)
    return res


#组合3
#字典序 (二进制排序) 组合
#将 nums 初始化为从 1 到 k的整数序列。 将 n + 1添加为末尾元素，起到“哨兵”的作用。
#将指针设为列表的开头 j = 0.
#While j < k :
#将nums 中的前k个元素添加到输出中，换而言之，除了“哨兵”之外的全部元素。
#找到nums中的第一个满足 nums[j] + 1 != nums[j + 1]的元素，并将其加一
#nums[j]++ 以转到下一个组合。
def combine3(n:int,k:int):
    # init first combination
    nums=list(range(1,k+1))+[n+1]
    res,j=[],0
    while j<k:
        # add current combination
        res.append(num[:k])
        j=0
        while j<k and num[j+1]==num[j]+1:
            num[j]=j+1
            j+=1
        nums[j]+=1
    return res
