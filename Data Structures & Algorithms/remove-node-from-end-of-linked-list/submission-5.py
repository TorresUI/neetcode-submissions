# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(0, head)
        l = dummyNode
        r = l
        for i in range(n):
            r = r.next
        
        #Now r is offset
        while r.next:
            l = l.next
            r = r.next
        
        #Now l is positioned 1 behind the nth position
        l.next = l.next.next if l.next else None

        return dummyNode.next