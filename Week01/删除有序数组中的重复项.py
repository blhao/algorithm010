#删除有序数组中的重复项
def deleteDuplicate(arr:list):
    i=len(arr)-1
    while i>=1:
        if arr[i] in arr[0:i]:
            arr.pop(i)
        i-=1
#删除有序数组中的重复项
#双指针，i 是慢指针，j是快指针
def removeDuplicate(arr:list):
    #倒序遍历
    i =len(arr)-1
    j = i-1
    while i>=1 and j>=0:
        #两个相邻的值如果不相同，i和j 都退一个位置
        if arr[j]!=arr[i]:
            i =j
        #如果相同，删除j所在的值，i所在的值的下标也变成i-1,j同时也退一个位置
        else:
            arr.pop(j)
            i-=1
        j-=1