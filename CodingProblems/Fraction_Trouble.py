# User function Template for python3
class Solution:
    def numAndDen(self, n, d):
        # code here
        a = 10 ** 4
        b = 10 ** 4
        num = 0
        den = 0
        ans = 0
        target = n / d

        while a > 0:
            res = a / b
            if res >= target:
                a -= 1
            else:
                if res > ans:
                    ans = res
                    num = a
                    den = b
                b -= 1

        return [num, den]
        # {
        #  Driver Code Starts
        # Initial Template for Python 3

        # Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, d = input().split()
        n = int(n)
        d = int(d)
        ob = Solution()
        ans = ob.numAndDen(n, d)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends
