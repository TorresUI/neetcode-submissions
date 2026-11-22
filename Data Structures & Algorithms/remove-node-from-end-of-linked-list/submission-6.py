# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head

        l, r = dummyNode, dummyNode
        while r.next and n:
            n -= 1
            r = r.next
        
        #now iterate both r and l until r reaches the end
        while r.next:
            l = l.next
            r = r.next
        
        #Now l should be positioned right before the target that we want to remove
        l.next = l.next.next
        return dummyNode.next
