# 寻找旋转排列数组中的最小值
'''
>>找到变化点，关于变化点的特点：
所有变化点左侧元素 > 数组第一个元素
所有变化点右侧元素 < 数组第一个元素
>>算法
1、找到数组的中间元素 mid。
2、如果中间元素 > 数组第一个元素，我们需要在 mid 右边搜索变化点。
3、如果中间元素 < 数组第一个元素，我们需要在 mid 做边搜索变化点。
4、当我们找到变化点时停止搜索，当以下条件满足任意一个即可：
nums[mid] > nums[mid + 1]，因此 mid+1 是最小值。
nums[mid - 1] > nums[mid]，因此 mid 是最小值。
'''


class Solution:
    def findMin(self, nums: list) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums)-1
        if nums[end] > nums[start]:
            return nums[start]
        while start <= end:
            mid = start+(start+end)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[start]:
                start = mid+1
            else:
                end = mid-1


#nums = [4,5,6,7,0,1,2]
nums = [3, 4, 5, 1, 2]
S = Solution()
S.findMin(nums)
