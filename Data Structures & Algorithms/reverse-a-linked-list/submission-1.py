# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        curr = head
        nexter = head.next
        curr.next = None

        while nexter:
            temp = nexter.next
            nexter.next = curr
            curr = nexter
            nexter = temp
        
        return curr