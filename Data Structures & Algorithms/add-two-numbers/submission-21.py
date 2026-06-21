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
        dummy = ListNode(0)
        dummy_temp = dummy

        while temp1 or temp2:
            ll1_val = temp1.val if temp1 else 0
            ll2_val = temp2.val if temp2 else 0

            curr_digit = ll1_val + ll2_val + carry
            carry = False

            if curr_digit >= 10:
                curr_digit %= 10
                carry = True
            
            dummy_temp.next = ListNode(curr_digit)
            dummy_temp = dummy_temp.next
            temp1 = temp1.next if temp1 else False
            temp2 = temp2.next if temp2 else False
        
        if carry:
            dummy_temp.next = ListNode(1)

        return dummy.next

# l1=[9,9,9,9,9,9,9]
# l2=[9,9,9,9]
# dummy -> 
