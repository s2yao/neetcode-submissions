# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ret = dummy
        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            # get smaller
            if temp1.val > temp2.val:
                dummy.next = temp2
                temp2 = temp2.next
            else:                
                dummy.next = temp1
                temp1 = temp1.next
            dummy = dummy.next
            

        # find out who is left over
        if temp1:
            dummy.next = temp1
        else:
            dummy.next = temp2
            
        return ret.next