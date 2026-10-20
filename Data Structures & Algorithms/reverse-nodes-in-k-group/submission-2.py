# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_k_th(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        if k == 0:
            return curr
        return None
    
    def reverse(self, prev, start, k):
        # includes end
        curr_ptr = start
        curr_prev = prev
        for _ in range(k):
            curr_next = curr_ptr.next
            curr_ptr.next = prev
            prev = curr_ptr
            curr_ptr = curr_next
        
        return prev

    def observability(self, start):
        while start:
            print(start)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_end = None
        curr = head
        prev = None

        while curr:
            start = curr
            end = self.find_k_th(start, k - 1)
            if not end: break
            next_start = end.next
            new_head = self.reverse(next_start, start, k)
            if prev_end:
                prev_end.next = new_head
            else:
                head = new_head
            prev_end = start
            curr = next_start
        
        return head
        