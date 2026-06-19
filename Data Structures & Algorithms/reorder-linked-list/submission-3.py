# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ### get to the middle
        mid = head # the slow ptr
        fast = head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        # mid sits the center
        # start point from after mid
        start_point = mid.next
        mid.next = None

        ### reverse it
        prev = None
        curr = start_point

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
                
        # merge element from prev into main list
        prev_merge = head
        curr_merge = head.next
        temp_merge = prev
        while temp_merge:
            temp = temp_merge.next
            temp_merge.next = curr_merge
            prev_merge.next = temp_merge
            temp_merge = temp
            prev_merge = curr_merge
            curr_merge = curr_merge.next if curr_merge else None
        
        return