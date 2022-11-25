# User function Template for python3
class Solution:
    def numberOfSubsequences(self, text, pattern):
        # code here
        ans = 0
        m = len(text)
        n = len(pattern)
        visited = [False for _ in range(m)]

        for i in range(m):
            if text[i] == pattern[0] and not visited[i]:
                idx = 1
                for j in range(i + 1, m):
                    if idx == n:
                        break
                    if not visited[j] and text[j] == pattern[idx]:
                        idx += 1
                        visited[j] = True
                if idx == n:
                    ans += 1

        return ans

        # {
     # Driver Code Starts
        # Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())
        W = str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S, W))

# } Driver Code Ends
