# User function Template for python3

class Solution:
    def numoffbt(self, nums, n):
        # Your code goes here
        MOD = 1e9 + 7
        maxValue = max(nums)
        minValue = min(nums)
        ans = 0
        present = [False for _ in range(maxValue + 1)]
        dp = [0 for _ in range(maxValue + 1)]

        for num in nums:
            present[num] = True
            dp[num] = 1

        for i in range(minValue, maxValue + 1):
            if not present[i]:
                continue
            for j in range(2, maxValue + 1):
                if j > i or i * j > maxValue:
                    break
                parent = i * j
                if not present[parent]:
                    continue
                dp[parent] = (dp[parent] + (dp[i] * dp[j]) % MOD) % MOD
                if i != j:
                    dp[parent] = (dp[parent] + (dp[i] * dp[j]) % MOD) % MOD
            ans = (ans + dp[i]) % MOD

        return int(ans)

        # {
        # Driver Code Starts
        # Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.numoffbt(a, n))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
