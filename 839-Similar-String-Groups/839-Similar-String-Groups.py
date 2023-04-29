class Solution:

    def isSimilar(self, word1, word2) -> bool:

        diff_count = 0
        answer = True

        for ch1, ch2 in zip(word1, word2):

            if ch1 != ch2:

                diff_count += 1

            if diff_count > 2:

                answer = False
                break

        return answer 

    def numSimilarGroups(self, strs: List[str]) -> int:

        answer = 1
        visited = set()
        not_visited = strs[:]
        visited.add(not_visited.pop())

        cluster = [strs[-1]]
        prev_size = 1

        while len(visited) < len(strs):

            temp = []

            while not_visited:

                anagram = not_visited.pop()

                for ch in cluster:

                    if self.isSimilar(ch, anagram):

                        cluster.append(anagram)
                        visited.add(anagram)
                        break

                else:

                    temp.append(anagram)

            not_visited = temp

            if len(not_visited) == 0:

                break

            if prev_size == len(cluster):

                anagram = not_visited.pop()
                visited.add(anagram)
                cluster = []
                cluster.append(anagram)
                prev_size = 1
                answer += 1  

            else:
                prev_size = len(cluster)

        return answer
