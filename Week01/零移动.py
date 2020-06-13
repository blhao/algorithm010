#零移动
#j总是指向第一个0的位置
def zeroMoves_1(arr:list):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j]=arr[i]
            if i!=j:
                arr[i]=0
            j+=1
#零移动  先把非0数移动到正确位置，再把后面的位置用0填充
def zeroMoves_2(arr:list):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j]=arr[i]
            j+=1
    while j <len(arr):
        arr[j]=0
        j+=1