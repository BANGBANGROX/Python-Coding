# User function Template for python3

class Solution:
    def formCoils(self, n):
        # code here
        coil = [2 * n * (4 * n + 1)]
        move = 1

        for step in range(2, 4 * n, 2):
            for _ in range(step):
                coil.append(coil[-1] - 4 * n * move)
            for _ in range(step):
                coil.append(coil[-1] + move)
            move *= -1

        for _ in range(4 * n - 1):
            coil.append(coil[-1] + 4 * n)

        return [coil, [16 * n * n + 1 - x for x in coil]]

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ptr = ob.formCoils(n)

        for i in range(2):
            print(*ptr[i])
# } Driver Code Ends
