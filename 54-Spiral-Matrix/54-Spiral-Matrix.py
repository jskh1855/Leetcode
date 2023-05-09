class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output = []
        total = len(matrix) * len(matrix[0])
        count = 0
        level = 0
        width = len(matrix)-1

        while True:

            for i in range(level ,len(matrix[0])-level):

                output.append(matrix[level][i])
                count += 1
                if count == total:
                    return output

            for i in range(len(matrix)-width , width):

                output.append(matrix[i][len(matrix[0])-level-1])
                count += 1
                if count == total:
                    return output

            for i in range(len(matrix[0])-level-1, level-1, -1):
                
                print(len(matrix[0])-level-1, i)
                output.append(matrix[len(matrix)-level-1][i])
                count += 1
                if count == total:
                    return output

            for i in range(width-1 , len(matrix)-width-1, -1):

                output.append(matrix[i][level])
                count += 1
                if count == total:
                    return output

            level += 1
            width -= 1
