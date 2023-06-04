class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        stack = []
        stack.append(0)
        answer = 1
        visited = set()
        visited.add(0)

        while len(visited) < len(isConnected):

            if len(stack) < 1:

                answer += 1
                
                for num in range(len(isConnected)):

                    if num not in visited:
                        
                        visited.add(num)
                        stack.append(num)
                        break

            node = stack.pop()

            for i in range(len(isConnected[node])):

                if i not in visited and i != node and isConnected[node][i] == 1:

                    stack.append(i)
                    visited.add(i)

        return answer
