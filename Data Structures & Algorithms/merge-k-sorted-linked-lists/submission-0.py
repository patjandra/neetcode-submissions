# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortOut = []
        for lst in lists:
            while lst:
                sortOut.append(lst.val)
                lst = lst.next
        sortOut.sort()
        dummy = ListNode(0)
        curr = dummy
        for num in sortOut:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next