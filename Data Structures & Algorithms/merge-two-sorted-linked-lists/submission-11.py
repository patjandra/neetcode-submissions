# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged = ListNode(0)
        curr = merged
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        if not list1:
            curr.next = list2
        elif not list2:
            curr.next = list1

        return merged.next
