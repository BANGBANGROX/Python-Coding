# User function Template for python3

class Solution:
    def check(self, n: int, target: int) -> bool:
        res = 0

        while n > 0:
            res += n // 5
            n //= 5

        return res >= target

    def findNum(self, target: int):
        # Complete this function
        l = 1
        r = 5 * target + 1
        ans = -1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if self.check(mid, target):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends
