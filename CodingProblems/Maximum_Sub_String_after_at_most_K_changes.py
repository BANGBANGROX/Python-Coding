# User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        n = len(s)
        l = 0
        ans = 0
        maxChars = 0
        count = [0 for _ in range(256)]

        for r in range(0, n):
            count[ord(s[r])] += 1
            maxChars = max(maxChars, count[ord(s[r])])
            differentChars = r - l + 1 - maxChars
            if differentChars > k:
                count[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        k = int(input())
        ob = Solution()
        ans = ob.characterReplacement(s, k)
        print(ans)

# } Driver Code Ends
