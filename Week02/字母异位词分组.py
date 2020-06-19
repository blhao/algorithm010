#字母异位词分组
#给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#所有输入均为小写字母。
#不考虑答案输出的顺序。
#暴力求解
def anagramGroup_1(arr:list):
    if len(arr)==0  or len(arr)==1: return arr
    for i in arr:
        i = sorted(i)
    arr=sorted(arr)
    result=[]
    
    for i in range(len(arr)-1):
        tag=0
        for k in result:
            if arr[i] in k:
                tag =1
                break
        if tag ==0:
            tmp=[]
            tmp.append(arr[i])
            for j in range(i+1,len(arr)):
                if len(arr[i])!=len(arr[j]) or sorted(arr[i])!=sorted(arr[j]):
                    continue
                tmp.append(arr[j])
            result.append(tmp)   
    return result

 #字母异位词分组
#哈希函数
#生成一个dict，每个键 K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 K。
def anagramGroup_2(strs:list):
    if len(strs)==0:return []
    result={}
    for item in strs:
        key=tuple(sorted(item))
        result[key]=result.get(key,[])+[item]
    print(result)
    return list(result.values())

#字母异位词分组
#哈希函数
#生成一个dict，每个键 K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 K。
import collections
def anagramGroup_3(strs:list):
    ans=collections.defaultdict(list)
    for item in strs:
        ans[tuple(sorted(item))].append(item)
    return ans.values()

#字母异位词分组
#按计数分类,当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
import collections
def anagramGroup_4(strs:list):
    ans=collections.defaultdict(list)
    for item in strs:
        count=[0]*26
        for s in item:
            count[ord(s)-ord('a')]+=1
        ans[tuple(count)].append(item)
    return ans.values()