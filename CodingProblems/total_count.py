# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


class Solution:
    def totalCount(self, k: int, arr: list[int]) -> int:
        # code here
        answer: int = 0

        for num in arr:
            answer += num // k
            if num % k > 0:
                answer += 1

        return answer


# {
# Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalCount(k, arr)
        print(res)
        t -= 1


# } Driver Code Ends
