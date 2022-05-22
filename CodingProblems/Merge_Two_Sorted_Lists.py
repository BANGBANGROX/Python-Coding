from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode(0)
        resTail = resHead

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                resTail.next = list1
                list1 = list1.next
            else:
                resTail.next = list2
                list2 = list2.next
            resTail = resTail.next

        if list1 != None:
            resTail.next = list1
        else:
            resTail.next = list2

        return resHead.next
