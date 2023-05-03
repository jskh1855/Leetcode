class Solution:
    def arraySign(self, nums: List[int]) -> int:

        answer = 1

        for num in nums:

            answer *= num

        if answer > 0:

            return 1

        elif answer < 0:

            return -1

        else:

            return 0
