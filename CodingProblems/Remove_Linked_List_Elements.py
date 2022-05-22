from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ansHead = ListNode()
        ansTail = ansHead

        while head != None:
            if head.val == val:
                head = head.next
                continue
            ansTail.next = ListNode(head.val)
            ansTail = ansTail.next
            head = head.next

        return ansHead.next
