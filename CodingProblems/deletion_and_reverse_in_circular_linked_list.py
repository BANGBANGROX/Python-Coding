# User function Template for python3
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        # code here
        nums = []
        curr = head

        nums.append(curr.data)
        curr = curr.next

        while curr != head:
            nums.append(curr.data)
            curr = curr.next

        nums.reverse()

        head = Node(-1)
        tail = head

        for num in nums:
            tail.next = Node(num)
            tail = tail.next

        tail.next = head.next

        return head.next

    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        # code here
        nums = []
        curr = head
        is_key_present = False

        nums.append(curr.data)
        curr = curr.next

        while curr != head:
            if curr.data == key:
                is_key_present = True
            nums.append(curr.data)
            curr = curr.next

        if is_key_present:
            nums.remove(key)

        head = Node(-1)
        tail = head

        for num in nums:
            tail.next = Node(num)
            tail = tail.next

        tail.next = head.next

        return head.next


# {
# Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends
