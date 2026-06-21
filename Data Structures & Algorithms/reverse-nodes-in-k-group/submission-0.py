class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1. Find the kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # 2. Reverse this group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 3. Reconnect reversed group
            oldGroupHead = groupPrev.next
            groupPrev.next = kth
            groupPrev = oldGroupHead