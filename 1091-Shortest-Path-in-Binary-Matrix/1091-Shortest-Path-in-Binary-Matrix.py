from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        que = deque([])
        que.append((0,0,1))
        eight_direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        n = len(grid)
        dp = [[n*n+1 for _ in range(n)] for _ in range(n)]
        answer = n*n+1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:

            return -1

        dp[0][0] = 1

        while que:

            x, y, length = que.popleft()

            if x == n-1 and y == n-1:

                break

            for dx, dy in eight_direction:

                if 0 <= x+dx < n and 0 <= y+dy < n:

                    if grid[x+dx][y+dy] == 1:

                        continue

                    if length+1 >= dp[x+dx][y+dy]:

                        continue

                    que.append((x+dx, y+dy, length+1))
                    dp[x+dx][y+dy] = length+1

        answer = dp[n-1][n-1]

        if answer == n*n+1:

            answer = -1

        return answer
