# User function Template for python3
class Solution:
    def reverseSpiral(self, m, n, matrix):
        # code here
        ans = []
        firstRow = 0
        lastRow = m - 1
        firstCol = 0
        lastCol = n - 1

        while firstRow <= lastRow and firstCol <= lastCol:
            # Firs row
            for i in range(firstCol, lastCol + 1):
                ans.append(matrix[firstRow][i])
            firstRow += 1
            if firstRow > lastRow:
                break
            # Last Col
            for i in range(firstRow, lastRow + 1):
                ans.append(matrix[i][lastCol])
            lastCol -= 1
            if firstCol > lastCol:
                break
            # Last Row
            for i in range(lastCol, firstCol - 1, -1):
                ans.append(matrix[lastRow][i])
            lastRow -= 1
            # First Col
            for i in range(lastRow, firstRow - 1, -1):
                ans.append(matrix[i][firstCol])
            firstCol += 1

        ans.reverse()

        return ans


        # {
     # Driver Code Starts
        # Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        R, C = [int(x) for x in input().split()]
        a = [[0]*C for c in range(R)]
        arr = input().split()
        for i in range(R*C):
            a[i//C][i % C] = int(arr[i])

        ob = Solution()
        ans = ob.reverseSpiral(R, C, a)
        for i in range(len(ans)):
            print(ans[i], end=" ")

        print()
# } Driver Code Ends
