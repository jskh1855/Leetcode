class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:

        num_of_closed_island = 0
        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(1, len(grid)-1):

            for j in range(1, len(grid[0])-1):

                if grid[i][j] == 0:

                    stack = []
                    stack.append((i,j))
                    on_edge = False
                    grid[i][j] = 1

                    while stack:

                        x, y = stack.pop()


                        for dx, dy in direction:

                            if grid[x+dx][y+dy] == 1:

                                continue

                            if x+dx == 0 or x+dx == len(grid)-1:

                                on_edge = True
                                grid[dx][dy] = 1
                                continue

                            if y+dy == 0 or y+dy == len(grid[0])-1:

                                on_edge = True
                                grid[dx][dy] = 1
                                continue

                            grid[x+dx][y+dy] = 1
                            stack.append((x+dx, y+dy))

                    if not on_edge:

                        num_of_closed_island += 1

        return num_of_closed_island
