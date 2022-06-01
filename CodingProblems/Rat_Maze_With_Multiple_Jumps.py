# User function Template for python3

class Solution:
    def dfs(self, matrix, x, y):
        if x == self.n - 1 and y == self.n - 1:
            self.res[x][y] = 1
            self.pathFound = True
            return

        if x < 0 or y < 0 or x >= self.n or y >= self.n or matrix[x][y] == 0:
            return

        # Mark the block visited
        self.res[x][y] = 1

        for i in range(1, matrix[x][y] + 1):
            self.dfs(matrix, x, y + i)
            if self.pathFound:
                return
            self.dfs(matrix, x + i, y)
            if self.pathFound:
                return

        # Unmark the block
        self.res[x][y] = 0

    def ShortestDistance(self, matrix):
        # Code here
        self.n = len(matrix)
        self.pathFound = False
        self.res = [[0 for _ in range(self.n)] for __ in range(self.n)]

        self.dfs(matrix, 0, 0)

        if not self.pathFound:
            return [[-1]]

        return self.res
        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for i in range(n):
            a = list(map(int, input().split()))
            matrix.append(a)
        ob = Solution()
        ans = ob.ShortestDistance(matrix)
        for i in ans:
            for j in i:
                print(j, end=" ")
            print()

# } Driver Code Ends
