#两数之和
#暴力
def twoSum_1(arr:list,k:int):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j])==k:
                return i,j
    return - 1
#两数之和
#字典生成哈希表
def twoSum_2(arr:list,k:list):
    hashmap = {}
    for i in range(len(arr)):
        if (k-arr[i]) in hashmap:
            print(i,hashmap[k-arr[i]])
            return i,hashmap[k-arr[i]]
        else:
            hashmap[arr[i]] = i
    return -1