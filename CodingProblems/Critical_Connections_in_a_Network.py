from ast import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited = [False] * n;
        low = [0] * n;
        disc = [0] * n;
        graph = [[] for i in range(0, n)];
        ans = [];
        timer = [0];

        for connection in connections :
            u = connection[0];
            v = connection[1];
            graph[u].append(v);
            graph[v].append(u)    

        def dfs(node, timer, parent) :
            visited[node] = True;
            low[node] = timer[0];
            disc[node] = timer[0];
            timer[0] += 1;

            for child in graph[node] :
                if visited[child] == False :
                     dfs(child, timer, node);
                     low[node] = min(low[node], low[child]);
                     if low[child] > disc[node] :
                        ans.append([node, child]);
                elif child != parent :
                    low[node] = min(low[node], disc[child]);
                   

        dfs(0, timer, -1);        
        
        return ans;
