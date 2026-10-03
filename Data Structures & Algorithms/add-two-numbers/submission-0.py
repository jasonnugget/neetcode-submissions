# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''

        prev = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            num1 += str(prev.val)
            prev = prev.next

        num2 = ''

        prev = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            num2 += str(prev.val)
            prev = prev.next

        newSum = int(num1) + int(num2)

        newSum = str(newSum)

        res = ListNode(0, None)
        dummy = res
        for i in range(len(newSum) - 1, -1, -1):
            temp = ListNode(int(newSum[i]), None)
            dummy.next = temp
            dummy = dummy.next

        return res.next

