#最小堆的应用
#前 K 个高频元素
#1、首先建立一个元素值对应出现频率的哈希表，
#2、维护一个元素数目为 k的最小堆
#每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
#如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
#最终，堆中的 k 个元素即为前 k 个高频元素
from collections import deque
class small_heap:
    #调整数值位置，成为小顶堆
    def heap_adjust(self,count,start,end):
        tmp=count[start]
        i=start
        j=i*2
        while j<=end:
            #根据数组出现频率大小比较，小的在堆顶
            if j<end and count[j][1]>count[j+1][1]:
                j+=1
            if tmp[1]>count[j][1]:
                count[i]=count[j]
                i=j
                j=i*2
            else:break
        count[i] = tmp
        return count
    def heap_create(self,count,k):
        #生成一个k大小的小顶堆
        first_start=k//2
        for i in range(first_start):
            self.heap_adjust(count,first_start-i,k)
        return count
    def topKFrequent(self,arr,k):
        if (not arr) or (k<=0) or (k>len(arr)):return 0
        count={}
        topOne=arr[0]
        frequent=1
        # #首先建立一个元素值对应出现频率的哈希表
        #同时获取出现频率第一的数值topOne
        for i in arr:
            key=i
            count[key]=count.get(key,0)+1
            if frequent<count[key]:
                topOne=arr[i]
                frequent=count[key]
        if k==1:
            return topOne
        elif k==len(count):
            return count.keys()
        elif 1<k<len(count):
            #创建小顶堆
            count_keys = list(count.keys())
            count_values=list(count.values())
            count = []
            for i in range(len(count_keys)):
                count.append((count_keys[i],count_values[i]))
            count_init = count[0:k]
            count_init = deque(count_init)
            count_init.appendleft((-1,-1))
            self.heap_create(count_init,k)
            #循环剩下的数，如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
            for i in range(k,len(count)):
                if count[i][1]>count_init[1][1]:
                    count_init[1] = count[i]
                    self.heap_adjust(count_init,1,k)
                else:
                    continue
            count_init.popleft()
            count =[]
            for i in count_init:
                count.append(i[0])
            return count
        else: return 0
        

#前 K 个高频元素
#使用现有的python库函数
#首先建立一个元素值对应出现频率的哈希表，可以用collections 中的Counter 函数生成
#维护一个元素数目为 k的最小堆
#每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
#如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
#最终，堆中的 k 个元素即为前 k 个高频元素
#在 Python 中可以使用 heapq 库中的 nlargest 方法，可以在相同时间内完成，但只需要一行代码解决
import collections
import heapq
def topKFrequent(arr,k):
    if (not arr) or (k<=0) or (k>len(arr)):return 0
    count=collections.Counter(arr)
    return heapq.nlargest(k, count.keys(), key=count.get)
    

#前 K 个高频元素
#哈希表按照频率排序，然后取前k个key值即可
def topKFrequent(arr,k):
    if (not arr) or (k<=0) or (k>len(arr)):return 0
    count={}
    topOne=arr[0]
    frequent = 1
    #首先建立一个元素值对应出现频率的哈希表
    #同时获取出现频率第一的数值topOne
    for i in arr:
        key=i
        count[key] = count.get(key,0)+1
        if frequent < count[key]:
            topOne = key
            frequent = count[key]
    if k ==1:
        #如果k为1，直接返回tipOne
        return topOne
    elif k == len(count):
        #如果k等于哈希表count的长度，直接返回count的keys值
        return list(count.keys())
    elif 1<k<len(count):
        #为count按照出现频率的大小排序，前K个即为结果
        count = sorted(count.items(), key=lambda count : count[1], reverse=True)
        count_topK=[]
        for i in range(k):
            count_topK.append(count[i][0])
        return count_topK
    else:return 0