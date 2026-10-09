# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2

        carry = 0
        dummy = ListNode()
        temp = dummy

        while temp1 or temp2:
            val1 = 0
            val2 = 0
            if temp1:
                val1 = temp1.val
            if temp2:
                val2 = temp2.val

            curr_digit = val1 + val2 + carry
            print(curr_digit)

            carry = 0

            if curr_digit >= 10:
                carry = 1
                curr_digit %= 10
            
            new_node = ListNode(curr_digit)
            temp.next = new_node
            temp = temp.next
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        if carry:
            temp.next = ListNode(1)

        return dummy.next