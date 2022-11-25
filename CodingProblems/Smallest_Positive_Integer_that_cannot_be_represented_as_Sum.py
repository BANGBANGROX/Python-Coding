# User function Template for python3

class Solution:
    def smallestpositive(self, nums, n):
        # Your code goes here
        ans = 1

        nums.sort()

        for num in nums:
            if ans < num:
                return ans
            else:
                ans += num

        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array, n))


# } Driver Code Ends
