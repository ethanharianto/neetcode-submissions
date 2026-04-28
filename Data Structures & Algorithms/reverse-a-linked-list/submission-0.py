# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # keep track of the next node
            temp = curr.next
            # reroute pointer
            curr.next = prev
            # new previous
            prev = curr
            # go next
            curr = temp
        return prev

            
        