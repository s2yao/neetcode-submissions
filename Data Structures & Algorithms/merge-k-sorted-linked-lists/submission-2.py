import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use heap to decide which of the first layer is the correct node
        heap_min = []
        counter = 0 # to accomodate dumb ass python syntax

        # seed the heap with head nodes
        for ll in lists:
            if ll:
                heapq.heappush(heap_min, (ll.val, counter, ll))
                counter += 1

        dummy_ret = ListNode()
        dummy_temp = dummy_ret

        while heap_min:
            curr_min_node = heapq.heappop(heap_min)[2]
            dummy_temp.next = curr_min_node
            dummy_temp = dummy_temp.next

            if curr_min_node.next:
                heapq.heappush(heap_min, (curr_min_node.next.val, counter, curr_min_node.next))
                counter += 1
            
        return dummy_ret.next