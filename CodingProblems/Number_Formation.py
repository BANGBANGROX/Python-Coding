# User function Template for python3
class Solution:
    def getSum(self, x, y, z):
        # code here
        MOD = 1e9 + 7
        exactSum = [[[0 for _ in range(z + 1)] for __ in range(y + 1)] for ___ in range(x + 1)]
        exactNum = [[[0 for _ in range(z + 1)] for __ in range(y + 1)] for ___ in range(x + 1)]
        ans = 0

        exactNum[0][0][0] = 1

        for i in range(x + 1):
            for j in range(y + 1):
                for k in range(z + 1):
                    if i > 0:
                        exactSum[i][j][k] = (exactSum[i][j][k] + exactSum[i - 1][j][k]
                                             * 10 + exactNum[i - 1][j][k] * 4) % MOD
                        exactNum[i][j][k] = (exactNum[i][j][k] + exactNum[i - 1][j][k]) % MOD
                    if j > 0:
                        exactSum[i][j][k] = (exactSum[i][j][k] + exactSum[i][j - 1][k]
                                             * 10 + exactNum[i][j - 1][k] * 5) % MOD
                        exactNum[i][j][k] = (exactNum[i][j][k] + exactNum[i][j - 1][k]) % MOD
                    if k > 0:
                        exactSum[i][j][k] = (exactSum[i][j][k] + exactSum[i][j][k - 1]
                                             * 10 + exactNum[i][j][k - 1] * 6) % MOD
                        exactNum[i][j][k] = (exactNum[i][j][k] + exactNum[i][j][k - 1]) % MOD
                    ans = (ans + exactSum[i][j][k]) % MOD

        return int(ans)                # {


        # Driver Code Starts
        # Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, Z = map(int, input().split())
        ob = Solution()
        ans = ob.getSum(X, Y, Z)
        print(ans)
# } Driver Code Ends
