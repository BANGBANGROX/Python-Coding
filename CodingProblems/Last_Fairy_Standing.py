import sys

sys.setrecursionlimit(100000)


class Solution:
    def last_fairy_standing(self, n: int, k: int) -> int:
        if n == 1:
            return 1

        return (self.last_fairy_standing(n - 1, k) + k - 1) % n + 1


# code here


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        k = int(input())

        obj = Solution()
        res = obj.last_fairy_standing(n, k)

        print(res)

# } Driver Code Ends
