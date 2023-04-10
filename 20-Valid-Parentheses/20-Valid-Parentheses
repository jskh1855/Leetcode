class Solution:
    def isValid(self, s: str) -> bool:
        
        thrower = list(s)
        receiver = []

        pairs = {'(':')', '{':'}', '[':']'}

        while thrower:

            parenthesis = thrower.pop()

            if len(receiver) == 0:

                receiver.append(parenthesis)
                continue

            if receiver[-1] != pairs.get(parenthesis, 'unavailable'):

                receiver.append(parenthesis)
                continue

            receiver.pop()

        if len(receiver) > 0:

            return False

        else:

            return True
