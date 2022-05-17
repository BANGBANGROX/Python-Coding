from ast import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid);

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1 : 
            return -1;
        
        visited = [[False] * 3 for i in range(0, n)];
        q = deque();
        ans = 1;
        dx = [-1, -1, 0, 1, 1, 1, 0, -1];
        dy = [0, 1, 1, 1, 0, -1, -1, -1];

        q.append((0, 0));
        visited[0][0] = True;

        while len(q) > 0 :
            size = len(q);
            for i in range(0, size) : 
                x, y = q.popleft();
                if x == n - 1 and y == n - 1 : 
                    return ans;
                for j in range(0, 8) :
                    newX = x + dx[j];
                    newY = y + dy[j];
                    if newX >= 0 and newY >= 0 and newX < n and newY < n and visited[newX][newY]  == False and grid[newX][newY] == 0 :
                        q.append((newX, newY));
                        visited[newX][newY] = True;
            ans += 1;

        return -1;         
