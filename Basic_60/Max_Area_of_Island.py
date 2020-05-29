from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        flag = [[0 for _ in range(m)] for _ in range(n)]
        dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0

        for j in range(n):  # y方向
            for i in range(m):  # x方向
                if grid[j][i] == 1 and flag[j][i] == 0:
                    tmp = 1
                    flag[j][i] = 1
                    stack = deque()
                    stack.append((j, i))
                    while stack != deque():
                        j, i = stack.pop()
                        for y, x in dd:
                            new_j = j + y  # 4方向調べないといけないのでnew_jとする
                            new_i = i + x
                            if 0 <= new_j < n and 0 <= new_i < m and grid[new_j][new_i] == 1 and flag[new_j][
                                new_i] == 0:
                                tmp += 1
                                flag[new_j][new_i] = 1
                                stack.append((new_j, new_i))
                    ans = max(ans, tmp)
        return ans
