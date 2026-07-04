# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.reverse()
        newList = ListNode()
        head = newList
        for num in arr:
            head.next = ListNode(num)
            head = head.next
        return newList.next

        