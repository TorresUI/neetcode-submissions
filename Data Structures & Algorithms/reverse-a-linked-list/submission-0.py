# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedList = None
        curr = head
        while curr != None:
            pnext = curr.next
            curr.next = reversedList
            reversedList = curr
            curr = pnext
        return reversedList
