# User function Template for python3

class Solution:
    def isPossible(self, adj_matrix: list) -> int:
        # Code here
        for path in adj_matrix:
            if sum(path) % 2 == 1:
                return 0

        return 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        paths = []
        for _ in range(n):
            cur = list(map(int, input().split()))
            paths.append(cur)
        obj = Solution()
        ans = obj.isPossible(paths)
        print(ans)

# } Driver Code Ends
