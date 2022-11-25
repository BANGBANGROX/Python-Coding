# User function Template for python3
class Solution:
    def minPoints(self, points, m, n):
        # code here
        points[m - 1][n - 1] = min(points[m - 1][n - 1], 0)

        for i in range(m - 2, -1, -1):
            points[i][n - 1] = min(points[i][n - 1] + points[i + 1][n - 1], 0)

        for i in range(n - 2, -1, -1):
            points[m - 1][i] = min(points[m - 1][i] + points[m - 1][i + 1], 0)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                points[i][j] = min(0, points[i][j] + max(points[i + 1][j], points[i][j + 1]))

        return abs(points[0][0]) + 1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n = input().split()
        m, n = int(m), int(n)
        points = []
        for _ in range(m):
            temp = [int(x) for x in input().split()]
            points.append(temp)
        ob = Solution()
        ans = ob.minPoints(points, m, n)
        print(ans)


# } Driver Code Ends
