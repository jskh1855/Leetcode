class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = ''
        i = 0

        while i < len(word1) and i < len(word2):

            merged += word1[i] + word2[i]
            i += 1

        if len(word1) == len(word2):

            return merged

        if len(word1) > len(word2):

            return merged + word1[i:]

        if len(word2) > len(word1):

            return merged + word2[i:]   
