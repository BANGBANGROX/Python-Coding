#User function Template for python3

class Solution:
    def __init__(self):
        self.answer = list()
        self.graph = list()
        self.discovery_time = list()
        self.lower_time = list()
        self.visited = list()
        self.timer = None

    def _find_bridges(self, node: int, parent: int):
        self.visited[node] = True
        self.discovery_time[node] = self.lower_time[node] = self.timer
        self.timer += 1

        for child in self.graph[node]:
            if child == parent:
                continue
            if self.visited[child]:
                self.lower_time[node] = min(self.lower_time[node], self.discovery_time[child])
            else:
                self._find_bridges(child, node)
                self.lower_time[node] = min(self.lower_time[node], self.lower_time[child])
                if self.discovery_time[node] < self.lower_time[child]:
                    self.answer.append([min(child, node), max(child, node)])

    def criticalConnections(self, n: int, graph: list) -> list:
        # code here
        self.graph = graph
        self.discovery_time = [0] * n
        self.lower_time = [0] * n
        self.visited = [False] * n
        self.timer = 0

        self._find_bridges(0, -1)
        self.answer.sort()

        return self.answer

#{
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends