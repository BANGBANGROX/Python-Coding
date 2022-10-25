# User function Template for python3
class Solution:
    def check(self, n, m, edges):
        # code here
        adjMatrix = [[False for __ in range(1 << n)] for _ in range(n)]
        dp = [[False for __ in range(1 << n)] for _ in range(n)]

        for edge in edges:
            u = edge[0] - 1
            v = edge[1] - 1
            adjMatrix[u][v] = True
            adjMatrix[v][u] = True

        for i in range(n):
            dp[i][1 << i] = True

        for i in range(1 << n):
            for j in range(n):
                if i & (1 << j) > 0:
                    for k in range(n):
                        if i & (1 << k) > 0 and adjMatrix[j][k] and k != j and dp[k][i ^ (1 << j)]:
                            dp[j][i] = True
                            break

        for i in range(n):
            if dp[i][(1 << n) - 1]:
                return True

        return False
        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        Edges = []
        e = list(map(int, input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i], e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends
