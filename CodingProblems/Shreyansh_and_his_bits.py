class Solution:
    def nCr(self, n, r):
        ans = 1

        for i in range(r):
            ans *= (n - i)
            ans /= (i + 1)

        return ans

    def count(self, n):
        # code here
        ans = 0
        pos = 0
        ones = 0

        while n > 0:
            if n % 2 == 1:
                ones += 1
                ans += self.nCr(pos, ones)
            pos += 1
            n >>= 1

        return ans

        # {
     # Driver Code Starts
if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(ob.count(N))


# } Driver Code Ends
