class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        answer = 0
        a_bit = bin(a).replace("0b", "")
        b_bit = bin(b).replace("0b", "")
        c_bit = bin(c).replace("0b", "")

        max_size = max(len(a_bit), len(b_bit), len(c_bit))
        
        a_diff = max_size - len(a_bit)
        b_diff = max_size - len(b_bit)
        c_diff = max_size - len(c_bit)

        a_bit = '0'*a_diff + a_bit
        b_bit = '0'*b_diff + b_bit
        c_bit = '0'*c_diff + c_bit

        for i in range(max_size):

            if c_bit[i] == '0':

                if a_bit[i] == '1':

                    answer += 1

                if b_bit[i] == '1':

                    answer += 1

            else:

                if a_bit[i] == '0' and b_bit[i] == '0':

                    answer += 1

        return answer
