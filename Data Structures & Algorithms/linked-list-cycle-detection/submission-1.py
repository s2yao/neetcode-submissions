# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer
        fast = head
        slow = head

        while fast and fast.next:
            # fast move 2 steps, slow move 1 step
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False