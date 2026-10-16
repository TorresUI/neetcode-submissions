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
        
        #Slow pointer is the last node in the first list

        secondList = s.next
        #Isolate the first list
        s.next = None

        #We want to reverse the secondList
        prev = None

        while secondList:
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp
        
        #Now we just need to change the order
        l1, l2 = head, prev

        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2