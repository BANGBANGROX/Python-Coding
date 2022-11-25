# User function Template for python3

class Solution:
    def countTriplets(self, nums):
        # Code here
        n = len(nums)
        ans = 0

        for i in range(1, n - 1):
            smaller = 0
            larger = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    smaller += 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    larger += 1
            ans += smaller * larger

        return ans

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.countTriplets(nums)
        print(ans)

# } Driver Code Ends
