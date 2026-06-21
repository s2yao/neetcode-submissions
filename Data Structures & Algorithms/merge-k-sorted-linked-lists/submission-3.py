import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        def combine(ll1: List[Optional[ListNode]], ll2: List[Optional[ListNode]]):
            dummy_ret = ListNode()
            dummy_temp = dummy_ret
            temp1 = ll1
            temp2 = ll2

            while temp1 and temp2:
                if temp1.val > temp2.val:
                    dummy_temp.next = temp2
                    temp2 = temp2.next
                else:
                    dummy_temp.next = temp1
                    temp1 = temp1.next

                dummy_temp = dummy_temp.next
            
            # if one longer
            if temp1:
                dummy_temp.next = temp1
            else:
                dummy_temp.next = temp2

            return dummy_ret.next

        # divide and conquer
        process = list(lists)

        while len(process) > 1:
            merged = []
            while len(process) >= 2:
                l1 = process.pop()
                l2 = process.pop()
                merged.append(combine(l1, l2))

            if len(process) == 1:
                merged.append(process.pop())
            
            process = merged
        
        return process[0]