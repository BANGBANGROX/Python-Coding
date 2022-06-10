# User function Template for python3

class Solution:
    def maxCoins(self, plates, coins, maxPlates, n):
        # code here
        ratios = []
        ans = 0

        for i in range(n):
            coin = coins[i]
            ratios.append([coin, i])

        ratios.sort()
        ratios.reverse()

        # print(ratios)

        for i in range(n):
            if plates[ratios[i][1]] <= maxPlates:
                ans += plates[ratios[i][1]] * ratios[i][0]
                maxPlates -= plates[ratios[i][1]]
            else:
                ans += ratios[i][0] * maxPlates
                break

        return int(ans)

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        T, N = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.maxCoins(A, B, T, N))
# } Driver Code Ends
