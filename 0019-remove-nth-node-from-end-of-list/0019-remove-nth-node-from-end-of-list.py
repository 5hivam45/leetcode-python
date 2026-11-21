class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next