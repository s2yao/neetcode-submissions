import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push the head of each non-empty linked list.
        # i is used as a tie-breaker because ListNode objects are not directly comparable.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Save next before detaching node.
            next_node = node.next

            # Detach node so we append exactly one node, not its old tail.
            node.next = None

            # Append current smallest node.
            tail.next = node
            tail = tail.next

            # Push the next node from the same original list.
            if next_node:
                heapq.heappush(heap, (next_node.val, i, next_node))

        return dummy.next