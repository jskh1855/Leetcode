class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        count = 1
        direction = [(1,0) ,(0,1) ,(-1,0) ,(0,-1) ]
        starting_point = set()
        ending_point = set()

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:

                    count += 1
                    stack = []
                    stack.append((i,j))
                    grid[i][j] = count

                    while stack:

                        x,y = stack.pop()

                        for dx,dy in direction:

                            if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]):

                                if grid[x+dx][y+dy] == 1:

                                    grid[x+dx][y+dy] = count
                                    stack.append((x+dx, y+dy))

                                if grid[x+dx][y+dy] == 0 and count == 2:

                                    starting_point.add((x, y))

                                if grid[x+dx][y+dy] == 0 and count == 3:

                                    ending_point.add((x, y))

                if count >= 3:

                    break

        answer = len(grid)*len(grid[0])

        for x1,y1 in list(starting_point):

            for x2,y2 in list(ending_point):

                dist = abs(x1-x2)+abs(y1-y2)-1
                answer = min(answer, dist)

        return answer
