# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = False
        ret = ListNode(0)
        temp_ret = ret

        while temp1 or temp2:
            if not temp1:
                target1 = 0
                target2 = temp2.val
            if not temp2:
                target1 = temp1.val
                target2 = 0
            else:
                target1 = temp1.val if temp1 else 0
                target2 = temp2.val if temp2 else 0

            curr_sum = target1 + target2 + carry
            carry = False
            if curr_sum >= 10:
                curr_sum = curr_sum % 10
                carry = True
            
            new_node = ListNode(curr_sum)
            temp_ret.next = new_node
            temp_ret = new_node
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        
        if carry:
            temp_ret.next = ListNode(1)
        
        return ret.next




