# 搜索旋转排序数组
# 二分搜索
# 思路：找到数组的中间值mid，然后判断左右两边哪部分是有序的，如果左边是有序的，并且目标值在这个范围，则丢弃右边，在左边查找；
# 如果右边是有序的，且目标值在右边，则丢弃左边，在右边查找；
class Solution:
    def search(self, arr: list, target: int):
        if not arr:
            return -1
        start, end = 0, len(arr)-1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            if arr[start] <= arr[mid]:
                if arr[start] <= target < arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if arr[mid] < target <= arr[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1


#nums = [4,5,6,7,0,1,2]
#target = 0
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
S = Solution()
S.search(nums, target)
