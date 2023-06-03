from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = defaultdict(list)
        answer = max(informTime)

        for i in range(n):

            graph[manager[i]].append(i)

        stack = []
        stack.append((headID, informTime[headID]))

        while stack:

            cur_employee, time = stack.pop()

            for child in graph[cur_employee]:

                if len(graph[child]) > 0:

                    stack.append((child, time + informTime[child]))
                    continue

                answer = max(answer, time)

        return answer
