# Your task is to complete this function
# Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1: list[int], arr2: list[int]) -> int:
        # Code here
        m: int = len(arr1)
        n: int = len(arr2)
        i: int = 0
        j: int = 0
        sum1: int = 0
        sum2: int = 0
        answer: int = 0

        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                answer += arr1[i] + max(sum1, sum2)
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < m:
            sum1 += arr1[i]
            i += 1

        while j < n:
            sum2 += arr2[j]
            j += 1

        return answer + max(sum1, sum2)


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends
