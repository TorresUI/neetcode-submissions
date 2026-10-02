# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        s, f = head, head.next.next

        while f and f.next:
            if s == f:
                return True
            
            s = s.next
            f = f.next.next
        return False