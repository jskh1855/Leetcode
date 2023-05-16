# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        slow, fast = head, head

        for _ in range(1, k):
            fast = fast.next

        cur = fast

        while cur.next:
            slow = slow.next
            cur = cur.next

        fast.val, slow.val = slow.val, fast.val

        return head
