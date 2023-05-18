# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:

            return head

        prev_n = ListNode()
        prev_n.next = head
        cur_n = head
        head = prev_n

        while cur_n and cur_n.next is not None:

            next_n = cur_n.next
            next_next_n = next_n.next
            prev_n.next = next_n
            next_n.next = cur_n
            cur_n.next = next_next_n
            prev_n = cur_n
            cur_n = next_next_n
        
        head = head.next
            
        return head
