class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        pushed.reverse()
        popped.reverse()
        answer = True

        while len(popped) > 0:

            if len(stack) == 0:

                stack.append(pushed.pop())

            elif stack[-1] == popped[-1]:

                stack.pop()
                popped.pop()

            elif len(pushed) > 0:

                stack.append(pushed.pop())

            else:
                answer = False
                break

        return answer
