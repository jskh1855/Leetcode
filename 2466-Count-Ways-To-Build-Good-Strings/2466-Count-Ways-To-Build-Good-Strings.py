class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0 for _ in range(high+1)]
        dp[zero] += 1
        dp[one] += 1
        answer = 0
        modulo = 10**9+7

        for i in range(high+1):

            if dp[i] > 0:

                if i+zero <= high:
                    
                    dp[i+zero] += dp[i]%modulo

                if i+one <= high:

                    dp[i+one] += dp[i]%modulo

                if i >= low:

                    answer += dp[i]%modulo

        return answer%modulo
