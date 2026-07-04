# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # append each item of each list into array, sort array, create new linked list
        arr = []
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst = lst.next
        arr.sort()

        dummy = ListNode(0)
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
