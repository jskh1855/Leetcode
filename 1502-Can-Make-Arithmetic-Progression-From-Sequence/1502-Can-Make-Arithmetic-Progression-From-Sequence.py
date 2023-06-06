class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        diff = arr[1] - arr[0]
        answer = True

        for i in range(2,len(arr)):

            if arr[i] - arr[i-1] != diff:

                answer = False
                break

        return answer 
