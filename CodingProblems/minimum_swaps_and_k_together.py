# User function Template for python3


class Solution:
    def minSwap(self, arr: list[int], n: int, k: int) -> int:
        # Complete the function
        sub_array_size: int = 0
        greater_than_k: int = 0

        for num in arr:
            if num <= k:
                sub_array_size += 1

        for i in range(sub_array_size):
            if arr[i] > k:
                greater_than_k += 1

        answer: int = greater_than_k
        left: int = 0

        for right in range(sub_array_size, n):
            if arr[left] > k:
                greater_than_k -= 1
            if arr[right] > k:
                greater_than_k += 1
            left += 1
            answer = min(answer, greater_than_k)

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

for _ in range(int(input())):
    n: int = int(input())
    arr: list[int] = list(map(int, input().strip().split()))
    k: int = int(input())
    ob: Solution = Solution()
    ans: int = ob.minSwap(arr, n, k)
    print(ans)


# } Driver Code Ends
