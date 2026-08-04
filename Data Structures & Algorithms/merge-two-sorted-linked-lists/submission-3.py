# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy

        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            val1 = temp1.val
            val2 = temp2.val
            if val1 > val2:
                curr.next = temp2
                temp2 = temp2.next
                curr = curr.next
            else:
                curr.next = temp1
                temp1 = temp1.next
                curr = curr.next
        
        if not temp1:
            curr.next = temp2
        else:
            curr.next = temp1
        
        return dummy.next