# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1, temp2 = headA, headB
        while temp1 != temp2:
            if not temp1:
                temp1 = headA
            else:
                temp1 = temp1.next
            if not temp2:
                temp2 = headB
            else:
                temp2 = temp2.next

        return temp1
