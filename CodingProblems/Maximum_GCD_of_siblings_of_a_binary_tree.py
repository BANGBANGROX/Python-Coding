# User function Template for python3


class Solution:
    def findGCD(self, a, b):
        if b == 0:
            return a

        return self.findGCD(b, a % b)

    def maxBinTreeGCD(self, edges, n):
        # code here
        edges.sort()
        maxGCD = 0

        for i in range(n - 1):
            sibblings = [edges[i][1]]
            while i + 1 < n - 1 and edges[i][0] == edges[i + 1][0]:
                sibblings.append(edges[i + 1][1])
                i += 1
            if len(sibblings) != 2:
                continue
            maxGCD = max(maxGCD, self.findGCD(sibblings[0], sibblings[1]))

        return maxGCD

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []

        for i in range(N-1):
            u, v = map(int, input().split())
            arr.append([u, v])

        ob = Solution()
        print(ob.maxBinTreeGCD(arr, N))
# } Driver Code Ends
