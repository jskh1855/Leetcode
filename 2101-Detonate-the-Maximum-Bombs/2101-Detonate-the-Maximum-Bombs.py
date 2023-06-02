class Solution:
    def isInCircle(self, x1, y1, r, x2, y2) -> bool:

        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        return distance <= r 

    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        visited = set()
        
        answer = 1
        cluster = []
        i = -1

        for bomb in bombs:

            i += 1

            stack = []
            stack.append(tuple(bomb))
            count = 0
                
            while stack:

                x,y,r = stack.pop()
                j = -1          

                for bomb in bombs:

                    j += 1

                    if j in visited:

                        continue

                    x2,y2,r2 = bomb

                    if self.isInCircle(x,y,r, x2,y2):
                        
                        count += 1
                        visited.add(j)
                        stack.append((x2,y2,r2))

            answer = max(answer, count)
            visited = set()

        return answer
