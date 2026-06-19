# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the total length
        total_len = 0
        curr_count = head

        while curr_count:
            total_len += 1
            curr_count = curr_count.next
        
        # calcualte the traversal steps needed
        steps = total_len - n
        curr = head
        prev = None
        
        while steps:
            prev = curr
            curr = curr.next
            steps -= 1
        
        # ATP curr sits on top of removal
        # prev sits prev of curr
        if total_len - n == 0:
            return head.next
        
        prev.next = curr.next
        return head