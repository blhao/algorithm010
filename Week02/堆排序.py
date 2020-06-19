#由于数组下标是从0开始的，而树的节点从1开始，
#我们还需要引入一个辅助位置，Python提供的原始数据类型list实际上是一个线性表(Array),
#由于我们需要在序列最左边追加一个辅助位，线性表这样做的话开销很大，需要把数组整体向右移动，
#所以list类型没有提供形如appendleft的函数，但是在一个链表里做这种操作就很简单了，Python的collections库里提供了链表结构deque，
#最大堆
from collections import deque
class heap:
    def heap_adjust(self,arr,start,end):
        tmp=arr[start]
        i=start
        j=start*2
        while j<=end:
            if j<end and arr[j]<arr[j+1]:
                j=j+1
            if tmp<arr[j]:
                arr[i]=arr[j]
                i=j
                j=i*2
            else:
                break
        arr[i]=tmp
        return arr
    def heap_sort(self,arr):
        if (not arr) or (len(arr)<=2):
            return arr
        len_arr=len(arr)-1
        first_start=len_arr//2
        for i in range(first_start):
            self.heap_adjust(arr,first_start-i,len_arr)
        for i in range(len_arr-1):
            arr[1],arr[len_arr-i] = arr[len_arr-i],arr[1]
            self.heap_adjust(arr,1,len_arr-i-1)
        return arr