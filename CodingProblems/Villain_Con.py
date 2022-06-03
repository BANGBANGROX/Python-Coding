# User function Template for python3

class Solution:
    def dfs(self, node, graph, visited, colors):
        visited[node] = True
        maxColor = 0

        for child in graph[node]:
            if not visited[child]:
                self.dfs(child, graph, visited, colors)
            maxColor = max(maxColor, colors[child])

        colors[node] = maxColor + 1

    def minColour(self, n, m, mat):
        # code here
        graph = [[] for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        colors = [0 for _ in range(n + 1)]

        for edge in mat:
            u = edge[0]
            v = edge[1]
            graph[v].append(u)

        for i in range(1, n + 1):
            if not visited[i]:
                self.dfs(i, graph, visited, colors)

        return max(colors)
# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        mat = [[0]*2 for y in range(M)]
        for i in range(M):
            arr = input().split()
            mat[i][0] = int(arr[0])
            mat[i][1] = int(arr[1])

        ob = Solution()
        print(ob.minColour(N, M, mat))
# } Driver Code Ends
