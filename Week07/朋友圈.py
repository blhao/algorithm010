#DFS
class Solution:
    def findCircleNum(self, M:list) -> int:
        N = len(M)
        count = 0
        visited = set()
        
        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(N):
            if  i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count


s = Solution()
num = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
s.findCircleNum(num)
