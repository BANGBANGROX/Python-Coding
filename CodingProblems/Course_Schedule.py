# User function Template for python3

from collections import deque
import sys


class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        graph = [[] for i in range(0, n)]
        indegree = [0] * n
        ans = []

        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            graph[v].append(u)
            indegree[u] += 1

        q = deque()

        for i in range(0, n):
            if indegree[i] == 0:
                q.append(i)

        while len(q) > 0:
            node = q.popleft()
            ans.append(node)

            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        if len(ans) != n:
            return []

        return ans
        # {
        #  Driver Code Starts
        # Driver Program


sys.setrecursionlimit(10**6)


def check(graph, N, res):
    map = [0]*N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []

        for i in range(m):
            u, v = map(int, input().split())
            adj[v].append(u)
            prerequisites.append([u, v])

        ob = Solution()

        res = ob.findOrder(n, m, prerequisites)

        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
