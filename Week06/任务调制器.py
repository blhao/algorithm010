# 任务调度器
# 整体的解题步骤如下：
# 1、计算每个任务出现的次数
# 2、找出出现次数最多的任务，假设出现次数为 x
# 3、计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
# 4、计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
# 5、上述结果如果小于tasks的长度，则最后的结果为tasks的长度
class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        task_map = {}
        for task in tasks:
            task_map[task] = task_map.get(task, 0)+1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        max_task_count = task_sort[0][1]
        res = (max_task_count-1)*(n+1)
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        return max(res, length)


# tasks=['A','A','A','B','B','B','C','C','D','D','D','D']
tasks = ['A', 'A', 'A', 'B', 'B', 'B']
s = Solution()
s.leastInterval(tasks, 2)
