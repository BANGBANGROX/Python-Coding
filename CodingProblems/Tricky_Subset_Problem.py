# User function Template for python3

class Solution:
    def isPossible(self, start, n, target, nums):
        # code here
        newNums = []
        currentSum = 0

        newNums.append(start)

        for i in range(n):
            currentSum += (newNums[i] + nums[i])
            if currentSum > target:
                break
            newNums.append(currentSum)

        for i in range(len(newNums) - 1, -1, -1):
            if newNums[i] > target:
                continue
            target -= newNums[i]
            if target == 0:
                return 1

        return 0
# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])

        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends
