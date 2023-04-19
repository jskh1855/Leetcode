# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        answer = 0
        stack = []
        stack.append((0, root, 0))

        while stack:

            depth, tree_node, prev_direction = stack.pop()
            answer = max(answer, depth)

            if tree_node.right is not None:

                if prev_direction >= 0:

                    stack.append((1+depth, tree_node.right, -1))

                else:

                    stack.append((1, tree_node.right, -1))

            if tree_node.left is not None:

                if prev_direction <= 0:

                    stack.append((1+depth, tree_node.left, 1))

                else:

                    stack.append((1, tree_node.left, 1))      

        return answer
