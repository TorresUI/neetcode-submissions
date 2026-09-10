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
                break

            if not list2:
                newList.next = list1
                break

            if list1.val > list2.val:
                newList.next = list2
                list2 = list2.next
            elif list1.val < list2.val or list1.val == list2.val:
                newList.next = list1
                list1 = list1.next
            newList = newList.next

            
        return temphead.next