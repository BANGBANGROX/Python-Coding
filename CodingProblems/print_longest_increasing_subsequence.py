#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, n: int, nums: list) -> list:
        last_index = [-1] * n
        dp = [0] * n
        answer = []

        dp[0] = 1
        last_index[0] = 0

        for i in range(1, n):
            dp[i] = 1
            last_index[i] = i
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    last_index[i] = j

        max_ind = 0

        for i in range(1, n):
            if dp[i] > dp[max_ind]:
                max_ind = i

        while last_index[max_ind] != max_ind:
            answer.append(nums[max_ind])
            max_ind = last_index[max_ind]

        answer.append(nums[max_ind])

        answer.reverse()

        return answer
#{
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends