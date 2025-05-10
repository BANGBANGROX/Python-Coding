# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
class Solution:
    def longestSubarray(self, arr: list[int], k: int) -> int:
        first_index: dict[int, int] = {}
        n: int = len(arr)
        running_counter: int = 0
        answer: int = 0

        for i in range(n):
            if arr[i] > k:
                running_counter += 1
            else:
                running_counter -= 1
            if running_counter > 0:
                answer = i + 1
            if first_index.get(running_counter - 1) is not None:
                answer = max(answer, i - first_index[running_counter - 1])
            if first_index.get(running_counter) is None:
                first_index[running_counter] = i

        return answer


# Code Here


# {
# Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = [int(x) for x in input().strip().split()]
        k = int(input())

        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends