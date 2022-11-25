# User function Template for python3
class Solution:
    def leafNodes(self, nums, n):
        # code here
        stack = []
        ans = []

        stack.append(nums[0])

        for i in range(1, n):
            if nums[i] < stack[-1]:
                stack.append(nums[i])
            else:
                num = stack[-1]
                size = len(stack)
                while len(stack) > 0 and nums[i] > stack[-1]:
                    stack.pop()
                stack.append(nums[i])
                if size > len(stack):
                    ans.append(num)

        ans.append(stack[-1])

        return ans

        # {
        # Driver Code Starts
        # Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr, N)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
