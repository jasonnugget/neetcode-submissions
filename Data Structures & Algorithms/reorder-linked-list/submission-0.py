# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        prev = None
        slow.next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        list2 = prev

        starter = head

        while list2:
            temp1 = starter.next
            temp2 = list2.next
            starter.next = list2
            list2.next = temp1
            list2 = temp2
            starter = temp1



