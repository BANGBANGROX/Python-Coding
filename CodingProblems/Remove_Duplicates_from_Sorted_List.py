from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode(0)
        ansTail = ansHead

        while head != None:
            ansTail.next = ListNode(head.val)
            ansTail = ansTail.next
            while head.next != None and head.val == head.next.val:
                head = head.next
            head = head.next

        return ansHead.next
