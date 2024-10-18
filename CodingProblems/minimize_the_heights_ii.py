# User function Template for python3


class Solution:
    def getMinDiff(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()

        n: int = len(arr)
        overall_min_height: int = arr[0] + k
        overall_max_height: int = arr[n - 1] - k
        answer: int = arr[n - 1] - arr[0]

        for i in range(0, n - 1):
            current_min_height: int = min(overall_min_height, arr[i + 1] - k)
            current_max_height: int = max(overall_max_height, arr[i] + k)
            if current_min_height >= 0:
                answer = min(answer, current_max_height - current_min_height)

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc: int = int(input())
    while tc > 0:
        k: int = int(input())
        # n = int(input())
        arr: list[int] = list(map(int, input().strip().split()))
        ob: Solution = Solution()
        ans: int = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
