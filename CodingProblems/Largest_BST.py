# User function Template for python3

from collections import deque
import sys


class Solution:
    def largestBstUtil(self, root):
        if root == None:
            return [0, 0, int(1e9), -1 * int(1e9)]

        if root.left == None and root.right == None:
            return [1, 1, root.data, root.data]

        left = self.largestBstUtil(root.left)
        right = self.largestBstUtil(root.right)

        if left[0] > 0 and right[0] > 0:
            if root.data > left[3] and root.data < right[2]:
                newSize = left[1] + right[1] + 1
                newMin = min(root.data, left[2])
                newMax = max(root.data, right[3])
                return [1, newSize, newMin, newMax]

        return [0, max(left[1], right[1]), 0, 0]
    # Return the size of the largest sub-tree which is also a BST

    def largestBst(self, root):
        # code here
        ans = self.largestBstUtil(root)

        return ans[1]

        # {

        #  Driver Code Starts
sys.setrecursionlimit(1000000)


# Tree Node

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends
