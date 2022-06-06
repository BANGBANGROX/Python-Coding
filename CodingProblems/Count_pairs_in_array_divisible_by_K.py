# User function Template for python3

import sys
import io
import atexit


class Solution:
    def countKdivPairs(self, arr, n, k):
        # code here
        count = [0 for _ in range(k)]
        ans = 0

        for num in arr:
            count[num % k] += 1

        ans += (count[0] * (count[0] - 1) // 2)

        for i in range(1, k // 2 + 1):
            if i == k - i:
                ans += (count[i] * (count[i] - 1) // 2)
            else:
                ans += (count[i] * count[k - i])

        return ans

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.countKdivPairs(a, n, k))
# } Driver Code Ends
