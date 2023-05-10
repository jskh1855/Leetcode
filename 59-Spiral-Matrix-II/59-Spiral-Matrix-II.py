class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        output = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        level = 0
        width = n-1

        while True:

            for i in range(level ,n - level):
           
                count += 1
                output[level][i] = count
                if count == n**2:
                    return output

            for i in range(n-width , width):

                count += 1
                output[i][n - level - 1] = count
                if count == n**2:
                    return output

            for i in range(n-level-1, level-1, -1):

                count += 1               
                output[n-level-1][i] = count
                if count == n**2:
                    return output

            for i in range(width-1 , n-width-1, -1):

                count += 1
                output[i][level] = count
                if count == n**2:
                    return output

            level += 1
            width -= 1
