# User function Template for python3

from collections import defaultdict
import heapq
import sys
import io
import atexit


class Solution:

    # Function to return the sorted array.
    def nearlySorted(self, a, n, k):
        pq = []
        ans = []

        heapq.heapify(pq)

        for i in range(n):
            if len(pq) == k + 1:
                ans.append(heapq.heappop(pq))
            heapq.heappush(pq, a[i])

        while len(pq) > 0:
            ans.append(heapq.heappop(pq))

        return ans

        # code here

        # {
        #  Driver Code Starts
        # Initial Template for Python 3

        # Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(*ob.nearlySorted(a, n, k))

# } Driver Code Ends
