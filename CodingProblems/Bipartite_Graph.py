class Solution:
    def checkBipartite(self, node, adj, visited, color):
        visited[node] = True

        for child in adj[node]:
            if not visited[child]:
                color[child] = not color[node]
                if not self.checkBipartite(child, adj, visited, color):
                    return False
            elif color[node] == color[child]:
                return False

        return True

    def isBipartite(self, n, adj):
        # code here
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]

        for i in range(n):
            if not visited[i]:
                if not self.checkBipartite(i, adj, visited, color):
                    return False

        return True


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
