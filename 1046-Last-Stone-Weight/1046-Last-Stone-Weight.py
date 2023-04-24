import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        hq = [-n for n in stones]
        heapq.heapify(hq)

        while len(hq) > 1:

            x = heapq.heappop(hq)
            y = heapq.heappop(hq)

            if x < y:

                heapq.heappush(hq, x - y )

        if len(hq):

            return - heapq.heappop(hq)

        return 0
