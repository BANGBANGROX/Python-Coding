# User function Template for python3


class Solution:
    def __upper_bound(self, nums: list[int], left: int, right: int, key: int) -> int:
        answer = right + 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > key:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

    def median(self, matrix: list[list[int]], m: int, n: int) -> int:
        # code here
        max_value: int = -1
        min_value: int = 10**9

        for i in range(m):
            max_value = max(max_value, matrix[i][n - 1])
            min_value = min(min_value, matrix[i][0])

        left: int = min_value
        right: int = max_value
        required: int = (m * n + 1) // 2

        while left < right:
            mid: int = left + ((right - left) >> 1)
            current: int = 0
            for i in range(m):
                current += self.__upper_bound(
                    nums=matrix[i], left=0, right=n - 1, key=mid
                )
            if current < required:
                left = mid + 1
            else:
                right = mid

        return left


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    ob: Solution = Solution()
    t: int = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        matrix: list[list[int]] = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t: list[int] = [int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        ans: int = ob.median(matrix, r, c)
        print(ans)
        print("~")
# } Driver Code Ends
