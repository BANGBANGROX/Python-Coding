# User function Template for python3

import math


class Solution:
    def isItPossible(sef, s, t, m, n):
        # code here
        if m != n:
            return 0

        positionsOfS = []
        positionsOfT = []

        for i in range(m):
            if s[i] != '#':
                positionsOfS.append([s[i], i])
            if t[i] != '#':
                positionsOfT.append([t[i], i])

        if len(positionsOfS) != len(positionsOfT):
            return 0

        for i in range(len(positionsOfS)):
            if positionsOfS[i][0] != positionsOfT[i][0]:
                return 0
            if positionsOfS[i][0] == 'A':
                if positionsOfS[i][1] < positionsOfT[i][1]:
                    return 0
            if positionsOfS[i][0] == 'B':
                if positionsOfS[i][1] > positionsOfT[i][1]:
                    return 0

        return 1
        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, T = input().split()
        ob = Solution()
        print(ob.isItPossible(S, T, len(S), len(T)))
# } Driver Code Ends
