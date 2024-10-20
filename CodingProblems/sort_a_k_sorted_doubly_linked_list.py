# User function Template for python3
"""
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
"""


# A node of the doubly linked list
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


import heapq


class Solution:
    def sortAKSortedDLL(self, head: DLLNode, k: int) -> DLLNode:
        # Code Here
        pq: list[int] = []
        current: DLLNode = head
        running_head: DLLNode = head

        while current is not None:
            heapq.heappush(pq, current.data)
            if len(pq) > k:
                running_head.data = heapq.heappop(pq)
                running_head = running_head.next
            current = current.next

        while len(pq) > 0:
            running_head.data = heapq.heappop(pq)
            running_head = running_head.next

        return head


# {
# Driver Code Starts


# Function to insert a node at the end of the doubly linked list
def push(tail: DLLNode, new_data: int) -> DLLNode:
    new_node: DLLNode = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail

    if tail is not None:
        tail.next = new_node

    return new_node


# Function to print nodes in a given doubly linked list
def printList(head: DLLNode) -> None:
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Driver code
if __name__ == "__main__":
    t: int = int(input())  # Number of test cases
    for _ in range(t):
        arr: list[int] = list(map(int, input().split()))  # Read the input array
        k: int = int(input())  # Read the value of k

        head: DLLNode = DLLNode(arr[0])
        tail: DLLNode = head

        for i in range(1, len(arr)):
            tail = push(tail, arr[i])

        solution: Solution = Solution()
        sorted_head: DLLNode = solution.sortAKSortedDLL(head, k)
        printList(sorted_head)

# } Driver Code Ends
