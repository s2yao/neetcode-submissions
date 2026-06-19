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
                while temp2:
                    temp2_sum = (temp2.val + carry)
                    carry = False
                    if temp2_sum >= 10:
                        temp2_sum = temp2_sum % 10
                        carry = True
                    temp_ret.next = ListNode(temp2_sum)
                    temp2 = temp2.next
                    temp_ret = temp_ret.next
                break
            if not temp2:
                while temp1:
                    temp1_sum = (temp1.val + carry)
                    carry = False
                    if temp1_sum >= 10:
                        temp1_sum = temp1_sum % 10
                        carry = True
                    temp_ret.next = ListNode(temp1_sum)
                    temp1 = temp1.next
                    temp_ret = temp_ret.next
                break
            
            curr_sum = temp1.val + temp2.val + carry
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




