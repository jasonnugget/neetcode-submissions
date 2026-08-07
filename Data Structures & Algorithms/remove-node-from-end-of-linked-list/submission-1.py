# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        traverse = head
        prev = None
        while traverse:
            temp = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = temp

        head = prev
        count = 1
        prev = None
        trav = head
        
        while count <= n:
            if count == n:
                if trav.next:
                    temp = trav.next
                if prev:
                    prev.next = temp
                else:
                    head = temp
                count += 1

            else:
                prev = trav
                trav = trav.next
                count += 1

        traverse = head
        prev = None
        while traverse:
            temp = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = temp

        return prev

        
                