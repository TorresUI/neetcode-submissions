# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Slow pointer is the end of the first list.
        secondListHead = slow.next
        #Isolate the first part of the list
        slow.next = None

        #Now we need to reverse the list for the second list
        newHead, prev = secondListHead, None

        while newHead:
            temp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp
        
        #Now prev is the list reversed. We now have to combine the two together
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2