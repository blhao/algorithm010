#接雨水
#按列
#求每一列的水，我们只需要关注当前列，以及左边最高的墙，右边最高的墙就够了。
#每列能装水量是 左右最高墙的较小数减去此列的高度
def trap(arr:list):
    if not arr:return 0
    sum=0
    for i in range(1,len(arr)-2):
        max_left = max(arr[0:i])
        max_right = max(arr[(i+1):len(arr)])
        if arr[i]<min(max_right,max_left):
            sum+=(min(max_right,max_left)-arr[i])
    return sum
#继续思考其他解法