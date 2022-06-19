# User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

import sys
import io
import atexit


class Solution:
    def reverseBetween(self, head, m, n):
        # code here

        if m == n:
            return head

        start = None
        prevStart = None
        count = 1
        current = head

        while count <= m:
            if count == m - 1:
                prevStart = current
            if count == m:
                start = current
            current = current.next
            count += 1

        nextStart = start.next
        previous = start

        while count <= n:
            nextNode = nextStart.next
            nextStart.next = previous
            previous = nextStart
            nextStart = nextNode
            if count == n:
                start.next = nextNode
            count += 1

        if prevStart != None:
            prevStart.next = previous
            return head

        return previous


# {
#  Driver Code Starts
# Initial Template for Python 3
# Initial Template for Python 3
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        inp = list(map(int, input().split()))
        N = inp[0]
        m = inp[1]
        n = inp[2]

        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        ob = Solution()
        newhead = ob.reverseBetween(a.head, m, n)
        a.printList(newhead)
# } Driver Code Ends
