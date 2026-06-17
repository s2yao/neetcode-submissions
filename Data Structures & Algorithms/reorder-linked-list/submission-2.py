class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find the middle of the list
        mid = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next

        # reverse linked list after mid
        curr_reverse = mid.next
        mid.next = None

        prev = None
        curr = curr_reverse

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        mid = prev

        # assemble
        ptr1 = head
        ptr2 = mid

        while ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1 = temp1
            ptr2 = temp2

        return