# User function Template for python3

class Solution:
    def TotalCountUtil(self, index, currentSum):
        if index >= self.n:
            return 1

        if self.dp[index][currentSum] != -1:
            return self.dp[index][currentSum]

        temp = 0
        ans = 0

        for i in range(index, self.n):
            temp += (ord(self.s[index]) - ord('0'))
            if temp >= currentSum:
                ans += self.TotalCountUtil(i + 1, temp)

        self.dp[index][currentSum] = ans

        return ans

    def TotalCount(self, s):
        # Code here
        self.s = s
        self.n = len(s)

        sumOfDigits = 0

        for ch in s:
            sumOfDigits += (ord(ch) - ord('0'))

        self.dp = [[-1 for _ in range(sumOfDigits + 1)] for __ in range(self.n)]

        # print(len(self.dp))
        # print(len(self.dp[0]))

        return self.TotalCountUtil(0, 0)
# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.TotalCount(s)
        print(ans)
# } Driver Code Ends
