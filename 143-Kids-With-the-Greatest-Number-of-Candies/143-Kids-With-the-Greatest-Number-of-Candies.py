class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        answer = []
        maximum = max(candies)

        for candy in candies:

            answer.append(candy+extraCandies >= maximum)

        return answer
