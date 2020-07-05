# 模拟行走机器人
'''
1、dx= {0,1,0,-1};
   dy= {1,0,-1,0};
   dx,dy 要竖着对齐看
    - 向北，坐标轴上x不动，y+1, 即(0,1)
    - 向东，坐标轴上x+1，y不动, 即(1,0)
    - 向南，坐标轴上x不动，y-1, 即(0,-1)
    - 向西，坐标轴上x-1，y不动, 即(-1,0)
2、必须注意使用 集合 Set 作为对障碍物使用的数据结构，以便我们可以有效地检查下一步是否受阻。
set存储根据哈希值来排序，速度比列表要快很多（大概10000倍）    
3、我们将会存储机器人的位置和方向。如果机器人得到转弯的指令，我们就更新方向；否则就沿给定的方向走指定的步数。
'''


class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, di = 0, 0, 0
        obstaclesSet = set(map(tuple, obstacles))
        res = 0
        for cmd in commands:
            if cmd == -2:
                di = (di-1) % 4
            elif cmd == -1:
                di = (di+1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstaclesSet:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x*x+y*y)
        return res


#commands = [4,-1,3]
#obstacles = []
commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
S = Solution()
S.robotSim(commands, obstacles)
