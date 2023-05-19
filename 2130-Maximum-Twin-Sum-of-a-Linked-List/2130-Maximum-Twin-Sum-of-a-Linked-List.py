# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        max_twin_sum = 2

        size = 1
        cur = head
        values = []

        while cur and cur.next:
            
            values.append(cur.val)
            cur = cur.next
            size += 1

        values.append(cur.val)
        
        i = size//2
        j = i - 1

        while i < size:

            max_twin_sum = max(max_twin_sum, values[i]+values[j])
            i += 1
            j -= 1

        return max_twin_sum
