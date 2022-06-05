# User function template for Python

class Solution:
    def check(self, n, m, l, h, a, t):
        total = 0

        for i in range(n):
            finalSpeed = h[i] + a[i] * t
            if finalSpeed >= l:
                total += finalSpeed
                if total >= m:
                    return True

        return False

    def buzzTime(self, n, m, l, h, a):
        # code here
        l = 1
        r = max(l, m)
        ans = -1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if self.check(n, m, l, h, a, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

        # {
        #  Driver Code Starts
        # Initial template for Python


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, L = [int(x) for x in input().split()]
        H = [0 for x in range(N)]
        A = [0 for x in range(N)]
        for i in range(N):
            H[i], A[i] = [int(y) for y in input().split()]
        ob = Solution()
        print(ob.buzzTime(N, M, L, H, A))

# } Driver Code Ends
