# User function Template for python3

class Solution:
    def recreationalSpot(self, nums, n):
        # Your code goes here
        stack = []
        last = 0

        for i in range(n - 1, -1, -1):
            if nums[i] < last:
                return True
            while len(stack) > 0 and nums[i] > stack[len(stack) - 1]:
                last = stack.pop()
            stack.append(nums[i])

        return False


# {
  # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        if ob.recreationalSpot(arr, n):
            print("True")
        else:
            print("False")


# } Driver Code Ends
