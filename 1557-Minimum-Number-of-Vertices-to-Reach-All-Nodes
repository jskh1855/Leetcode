class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        appearance = [0 for num in range(n)]

        for begin, end in edges:

            appearance[end] = 1

        answer = []

        for i in range(n):

            if appearance[i] == 0:

                answer.append(i)

        return answer
