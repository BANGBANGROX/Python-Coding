# User function Template for python3
class Solution:
    def maxProduct(self, arr: list[int]) -> int:
        n: int = len(arr)
        max_value: int = arr[0]
        min_value: int = arr[0]
        answer: int = arr[0]

        for i in range(1, n):
            if arr[i] < 0:
                max_value, min_value = min_value, max_value
            max_value = max(arr[i], max_value * arr[i])
            min_value = min(arr[i], min_value * arr[i])
            answer = max(answer, max_value)

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc: int = int(input())
    while tc > 0:
        n: int = int(input())
        arr: list[int] = list(map(int, input().strip().split()))
        ob: Solution = Solution()
        ans: int = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
