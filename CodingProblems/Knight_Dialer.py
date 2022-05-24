class Solution:
    def knightDialerUtil(self, x: int, y: int, ind: int, n: int) -> int:
        if x > 3 or x < 0 or y < 0 or y > 2 or (x == 3 and y == 0) or (x == 3 and y == 2):
            return 0
        
        if ind == n:
            return 1

        if self.dp[ind][x][y] != -1:
            return self.dp[ind][x][y]

        ans = 0

        for i in range(8):
            newX = x + self.dx[i]
            newY = y + self.dy[i]
            ans = (ans + self.knightDialerUtil(newX, newY, ind + 1, n)) % self.mod

        self.dp[ind][x][y] = ans

        return ans

    def knightDialer(self, n: int) -> int:
        self.dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        self.dy = [1, 2, 2, 1, -1, -2, -2, -1]
        self.mod = int(1e9 + 7)
        self.dp = [[[-1] * 3 for i in range(4)] for i in range(n + 1)]
        ans = 0

        for i in range(4):
            for j in range(3):
                ans = (ans + self.knightDialerUtil(i, j, 1, n)) % self.mod

        return ans
