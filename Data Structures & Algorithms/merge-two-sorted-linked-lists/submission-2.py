# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newNode = ListNode(0, None)
        temp = newNode
        while list1 or list2:

            if list1 and list2:
                if list1.val > list2.val:
                    temp.next = list2
                    list2 = list2.next
                elif list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list1
                    list1 = list1.next
            
            else:
                if list1:
                    temp.next = list1
                    return newNode.next
                else:
                    temp.next = list2
                    return newNode.next

            temp = temp.next

        return newNode.next