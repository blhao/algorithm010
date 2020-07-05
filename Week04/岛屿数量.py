# 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
# 解法：深度优先搜索
# 两层遍历，遇到一个值为1的，count加1，然后把跟它属于同一个岛屿的位置都设置成0；
import collections


class Solution1:
    def numIslands(self, grid: list) -> int:
        def dfs(grid: list, i: int, j: int):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
                return
            grid[i][j] = 0
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        count = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    count += 1
        return count


# 广度优先遍历
# 遇到值为1的就入栈，遍历栈内元素，值设为0，上下左右的值都检查一次，值为1的入栈；
class Solution2:
    def numIslands(self, grid: list) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    count += 1
                    grid[i][j] = 0
                    queue = collections.deque([(i, j)])
                    while queue:
                        row, col = queue.popleft()
                        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= r < nr and 0 <= c < nc and grid[r][c] == 1:
                                grid[r][c] = 0
                                queue.append((r, c))
        return count


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
S = Solution2()
S.numIslands(grid)
