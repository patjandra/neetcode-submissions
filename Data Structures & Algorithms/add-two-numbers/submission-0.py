# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # go add each number in LLs, adding to front of string l1->num1 and l2->num2
        # convert num1 and num2 to ints and add them, and reverse it
        # run through new reversed num, and add to new LL using dummy node
        num1 = ''
        num2 = ''
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next
        summed = int(num1) + int(num2)
        numString = str(summed)[::-1]

        dummy = ListNode(0)
        curr = dummy
        for i in range(len(numString)):
            curr.next = ListNode(numString[i])
            curr = curr.next
        return dummy.next
