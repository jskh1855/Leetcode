class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        answer = 0
        i = -1
        j = len(mat)

        for k in range(len(mat)):

            i += 1
            j -= 1

            if i == j:

                answer += mat[k][i]
                continue

            answer += mat[k][i] + mat[k][j]

        return answer
