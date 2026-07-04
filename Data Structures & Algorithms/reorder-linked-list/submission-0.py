# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer and make 1st and 2nd halves
        # reverse 2nd half
        # merge 1st and 2nd parts
        # [1,2,3,4,5] | 1->2->3->None and 4->5->None | 5->4 | 1->5->2->4->3->None
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        second = slow.next # 2nd half of the linked list
        slow.next = None # head is start of 1st half
        prev = None

        while second: # reverse 2nd half
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first = head
        second = prev

        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2


        