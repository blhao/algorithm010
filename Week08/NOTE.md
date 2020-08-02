<pre>
#选择排序
def selectionSort(s:list):
    len_s = len(s)
    print(len_s)
    minIndex = 0
    tmp = 0
    i = 0
    while i < len_s-1:
        minIndex = i
        j = i+1
        while j < len_s:
            if s[j] < s[minIndex]:
                minIndex = j
            j = j + 1
        tmp = s[i]
        s[i] = s[minIndex]
        s[minIndex] = tmp
        i = i + 1
s = [9,8,7,6,5,4,3,2,1]
selectionSort(s)
print(s)
</pre>
<pre>
#插入排序
def insertSort(s:list):
    if not s:return 0
    len_s = len(s)
    r = []
    r.append(s[0])
    i = 1
    while i<len_s:
        k = len(r) - 1
        while k >=0:
            if s[i] < r[k]:
                k = k-1
            else:
                break
        r.insert(k+1,s[i])
        i = i+1
    return r
#s = [9,8,7,6,5,4,3,2,1]
#s = [3,2,6,9,4,1,7,3,2,8,0]
s = []
r = insertSort(s)
print(r)
</pre>
<pre>
#快速排序
class Solution:
    def quickSort(self,nums:list,low:int,high:int):
        if low < high:
            p = self.position(nums,low,high)
            self.quickSort(nums,low,p-1)
            self.quickSort(nums,p+1,high)
    def position(self,nums:list,low:int,high:int):
        i = low
        j = high
        tmp = nums[low]
        while(i <j):
            while(i<j and nums[j]>=tmp):
                j = j - 1
            nums[i] = nums[j]
            while(i<j and nums[i]<=tmp):
                i = i+1
            nums[j] = nums[i]
        nums[i] = tmp
        return i
</pre>
<pre>
#冒泡排序
def bubbleSort(s:list):
    if not s:return 0
    len_s = len(s)
    isChangd = True
    tmp = 0
    for i in range(len_s-1):
        isChangd = False
        for j in range(len_s-i-1):
            if s[j] > s[j+1]:
                tmp = s[j]
                s[j] = s[j+1]
                s[j+1] = tmp
                isChangd = True
        if isChangd == False:
            break
    return s
s = [9,8,7,6,5,4,3,2,1]
r = bubbleSort(s)
print(r)      
</pre>
<pre>
#堆排序
#大根堆：每个结点的值都大于或等于左右孩子结点
#小根堆：每个结点的值都小于或等于左右孩子结点
#如何把一个序列构造出一个大根堆
#输出堆顶元素后，如何使剩下的元素构造出一个大根堆
#详情请查看https://www.jianshu.com/p/d174f1862601
class solution:
    def swap_param(self,L:list,i:int,j:int):
        L[i],L[j] = L[j],L[i]
        return L
    def heap_adjust(self,L:list, start:int, end:int):
        tmp = L[start]
        i = start
        j = i*2
        while j <= end:
            if (j < end) and (L[j] < L[j+1]):
                j = j+1
            if tmp < L[j]:
                L[i] = L[j]
                i = j
                j = i*2
            else:
                break
        L[i] = tmp
        return L
    def heap_sort(self,L:list):
        if not L:return 0
        len_L = len(L)-1
        if len_L == 0:return 0
        first_sort_count = len_L//2
        for i in range(first_sort_count):
            self.heap_adjust(L,first_sort_count - i,len_L)
        for i in range(len_L - 1):
            self.swap_param(L,1,len_L - i)
            self.heap_adjust(L,1,len_L - i -1)
        return L
L = [0,50,16,30,10,60,90,2,80,70]        
X = solution()
X.heap_sort(L)
print(L[1:])
</pre>
<pre>
#归并排序x 
class solution:
    """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
    def merge(self,s1:list,s2:list,s:list):
        i =j = k = 0
        while i<len(s1) and j<len(s2):
            if s1[i] <= s2[j]:
                s[k] = s1[i]
                i = i+1
            else:
                s[k] = s2[j]
                j = j+1
            k = k+1
        while i == len(s1) and j<len(s2):
            s[k] = s2[j]
            j = j+1
            k = k+1
        while j == len(s2) and i<len(s1):
            s[k] = s1[i]
            i = i+1
            k = k+1
        return s
    def merge_sort(self,s):
        n = len(s)
        ## 剩一个或没有直接返回，不用排序
        if n < 2:
            return
        mid = n//2
        s1 = s[0:mid]
        s2 = s[mid:n]
        self.merge_sort(s1)
        self.merge_sort(s2)
        self.merge(s1,s2,s)
        return s
s = [1,7,3,5,4]
X = solution()
X.merge_sort(s)
print(s)
</pre>
<pre>
#希尔排序
def shell_sort(s:list):
    n = len(s)
    gap = n//2
    while gap >=1:
        for i in range(gap,n):
            j = i
            while (j-gap) >=0:
                if s[j] <s[j-gap]:
                    s[j],s[j-gap] = s[j-gap],s[j]
                    j -=gap
                else:
                    break
        gap//=2
s = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
shell_sort(s)
print(s)
</pre>
<pre>
#计数排序
def count_sort(arr:list):
    arr_max = max(arr)
    count = [0 for i in range(arr_max+1)]
    for i in arr:
        count[i] += 1
    for i in range(arr_max+1):
        if i >=1:
            count[i] += count[i-1]
    result = [0 for i in range(len(arr))]
    i = len(arr) -1
    while i >=0:
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -=1
        i -=1
    return result
arr = [4,2,1,8,5,4,3,0,0,9]
result = count_sort(arr)
print(result)
</pre>
<pre>
#桶sort+快速排序
class solution:
    def position(self,arr:list,low:int,high:int):
        i,j = low,high
        tmp = arr[i]
        while i < j:
            while i<j and arr[j] >=tmp:
                j -=1
            if i<j:
                arr[i] = arr[j]
                i +=1
            while i<j and arr[i] <=tmp:
                i +=1
            if i <j:
                arr[j] = arr[i]
                j -=1
        arr[i] = tmp
        return i
    def quick_sort(self,arr:list,low:int,high:int):
        if not arr:return 0
        if low < high:
            k = self.position(arr,low,high)
            self.quick_sort(arr,low,k-1)
            self.quick_sort(arr,k+1,high)
        return arr
    def bucket_sort(self,arr:list):
        max_num,min_num = max(arr),min(arr)
        bucketArr = [[] for i in range(max_num//10 - min_num//10 + 1)]
        for i in arr:
            index = i//10 - min_num//10
            bucketArr[index].append(i)
        arr.clear()
        for i in bucketArr:
            self.quick_sort(i,0,len(i)-1)
            arr.extend(i)
        return arr
x = solution()
arr = [-7,51,3,121,-3,32,21,43,4,25,56,77,16,22,87,56,-10,68,99,70]
x.bucket_sort(arr)
print(arr)
</pre>
<pre>
#基数排序
def radix_sort(arr:list):
    if not arr:return 0
    len_arr = len(arr)
    max_arr = max(arr)
    #列表中最大数的位数
    len_max_arr = len(str(max_arr))
    #把list中的整数位数对齐变成字符串形式
    for i in range(len(arr)):
        arr[i] = str(arr[i]).zfill(len_max_arr)
    k = len_max_arr -1
    while k >=0:
        bucketArr = [[] for i in range(10)]
        for i in arr:
            index = int(i[k])
            bucketArr[index].append(i) 
        arr.clear()
        for i in bucketArr:
            arr.extend(i)
        k -=1
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr
arr = [43,4,25,56,77,16,22,87,56,10,68,999,707,121,0]
radix_sort(arr)
print(arr)
</pre>
