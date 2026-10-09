# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        max_heap = []
        new_arr = []
        dummy = ListNode()
        temp = dummy
        
        for idx, llist in enumerate(lists):
            if not llist:
                continue
            condom = [llist.val, idx, llist]
            heapq.heappush(max_heap, condom)
        
        while max_heap:
            curr_val, idx, curr_list = heapq.heappop(max_heap)
            temp.next = ListNode(curr_val)
            temp = temp.next
            if curr_list.next:
                heapq.heappush(max_heap, [curr_list.next.val, idx, curr_list.next])

        
        return dummy.next