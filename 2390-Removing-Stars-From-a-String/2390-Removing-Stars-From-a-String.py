class Solution:
    def removeStars(self, s: str) -> str:

        stack = list(s)
        stars_removed = ''
        num_of_removal = 0

        while stack:

            char = stack.pop()

            if char == '*':

                num_of_removal += 1
                continue

            if num_of_removal > 0:

                num_of_removal -= 1
                continue

            stars_removed = char + stars_removed
            
        return stars_removed
