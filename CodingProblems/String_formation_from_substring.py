# User function Template for python3
class Solution:
    def isRepeat(self, s):
        # code here
        n = len(s)

        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[i:] == s[:n - i]:
                return 1

        return 0

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.isRepeat(s)

        print(answer)


# } Driver Code Ends
