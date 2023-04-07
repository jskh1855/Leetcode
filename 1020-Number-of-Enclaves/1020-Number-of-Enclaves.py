class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        num_of_land_cells = 0
        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(1, len(grid)-1):

            for j in range(1, len(grid[0])-1):

                if grid[i][j] == 1:

                    stack = []
                    stack.append((i,j))
                    on_edge = False
                    grid[i][j] = 0
                    count = 1

                    while stack:

                        x, y = stack.pop()


                        for dx, dy in direction:

                            if grid[x+dx][y+dy] == 0:

                                continue

                            if x+dx == 0 or x+dx == len(grid)-1:

                                on_edge = True
                                grid[dx][dy] = 0
                                continue

                            if y+dy == 0 or y+dy == len(grid[0])-1:

                                on_edge = True
                                grid[dx][dy] = 0
                                continue

                            grid[x+dx][y+dy] = 0
                            stack.append((x+dx, y+dy))
                            count += 1

                    if not on_edge:

                        num_of_land_cells += count

        return num_of_land_cells
