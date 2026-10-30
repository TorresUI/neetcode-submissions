# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        newHead = dummyNode

        while list1 or list2:
            if not list1:
                newHead.next = list2
                break
            
            if not list2:
                newHead.next = list1
                break
            
            if list1.val < list2.val:
                #Proccess the first list then the second
                temp = list1.next
                newHead.next = list1
                newHead = newHead.next
                list1 = temp
            else:
                temp2 = list2.next
                newHead.next = list2
                newHead = newHead.next
                list2 = temp2

        return dummyNode.next
        