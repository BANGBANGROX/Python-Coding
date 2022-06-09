# User function Template for python3


import sys
import io
import atexit


class Solution:

    def find(self, node, par):
        if par[node] != node:
            par[node] = self.find(par[node], par)
            return par[node]

        return node

    # Function to merge two nodes a and b.
    def union_(self, a, b, par, rank1):
        # code here
        parentA = self.find(a, par)
        parentB = self.find(b, par)

        if parentA == parentB:
            return

        if rank1[parentA] > rank1[parentB]:
            par[parentB] = parentA
            rank1[parentA] += rank1[parentB]

        else:
            par[parentA] = parentB
            rank1[parentB] += rank1[parentA]

        # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x, y, par, rank1):
        # code here
        parentX = self.find(x, par)
        parentY = self.find(y, par)

        return parentX == parentY

        # {
        #  Driver Code Starts
        # Initial Template for Python 3

        # Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        q = int(input())

        par = [i for i in range(n+1)]  # parent of ith node is initialized as i.
        rank1 = [1 for i in range(n+1)]  # rank is initialized as 1 fo every node
        obj = Solution()
        for i in range(q):
            task, u, v = map(str, input().strip().split())
            u = int(u)
            v = int(v)

            if task == 'U':
                obj.union_(u, v, par, rank1)
            else:
                if obj.isConnected(u, v, par, rank1):
                    print(1)
                else:
                    print(0)


# } Driver Code Ends
