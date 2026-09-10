# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temphead = ListNode(None)
        newList = temphead

        while list1 or list2:

            if not list1:
                newList.next = list2
                newList = newList.next
                if list2:
                    list2 = list2.next
                continue

            if not list2:
                newList.next = list1
                newList = newList.next
                if list1:
                    list1 = list1.next
                continue

            if list1.val > list2.val:
                newList.next = list2
                newList = newList.next
                list2 = list2.next
            elif list1.val < list2.val or list1.val == list2.val:
                newList.next = list1
                newList = newList.next
                list1 = list1.next
            
        return temphead.next