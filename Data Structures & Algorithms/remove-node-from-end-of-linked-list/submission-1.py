# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the list
        # counter
        # track curr and prev nodes
        # once counter hits n
            # set set prev.next to curr.next, set curr.next to None
        # reverse the list again

        if head.next == None:
            return None

        # reverse list
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # remove nth from reversed list
        reverse = prev
        count = 1
        curr = reverse
        prev = reverse
        if n == 1:
            reverse = prev.next
        else:
            while count != n and curr.next != None:
                count += 1
                curr = curr.next
            while prev.next != curr and prev.next != None:
                prev = prev.next
            prev.next = curr.next
            curr.next = None

        # reverse list to original
        curr = reverse
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
            

