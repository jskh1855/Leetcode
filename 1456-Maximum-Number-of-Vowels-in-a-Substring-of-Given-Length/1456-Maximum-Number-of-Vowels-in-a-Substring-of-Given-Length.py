class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}
        count_vowels = 0

        for i in range(k):

            if s[i] in vowels:

                count_vowels += 1

        max_count = count_vowels

        for j in range(len(s)-k):

            if s[j] in vowels:

                count_vowels -= 1

            if s[j+k] in vowels:

                count_vowels += 1

            max_count = max(max_count, count_vowels)

        return max_count
