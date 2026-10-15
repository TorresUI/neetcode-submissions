# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        #Now s.val should be the end of the first list.
        secondList = s.next
        s.next = None
        #Now we have isolated the first list and we have the head of the second list
        #Now we want to reverse the second list before we can merge both lists.

        prev = None
        while secondList:
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp
        
        #Now prev should be the head of the reversed list
        list1, list2 = head, prev

        list1, list2 = head, prev
        while list2:
            t1, t2 = list1.next, list2.next
            list1.next = list2
            list2.next = t1
            list1, list2 = t1, t2
        