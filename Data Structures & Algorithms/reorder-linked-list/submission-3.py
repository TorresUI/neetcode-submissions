# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        s = head
        f = head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        
        reverseHead = s.next
        #Set the end of the first list to null
        s.next = None

        #now we need to reverse the linked list
        prev = None

        while reverseHead:
            temp = reverseHead.next
            reverseHead.next = prev
            prev = reverseHead
            reverseHead = temp
        
        #Now prev is the new head
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            
            firstNext, secondNext = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = firstNext
            firstHalf, secondHalf = firstNext, secondNext
            

