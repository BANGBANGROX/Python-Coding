# User function Template for python3


class Solution:
    def __init__(self) -> None:
        self.__nums: list[int] = None
        self.__k: int = 0
        self.__dp: list[list[int]] = None

    def __solve_word_wrap_handler(self, idx: int, spaces_left: int) -> int:
        if idx >= len(self.__nums):
            return 0

        if self.__dp[idx][spaces_left] != -1:
            return self.__dp[idx][spaces_left]

        result: int = (
            self.__solve_word_wrap_handler(idx + 1, self.__k - self.__nums[idx])
            + spaces_left * spaces_left
        )

        if spaces_left > self.__nums[idx]:
            result = min(
                result,
                self.__solve_word_wrap_handler(idx + 1, spaces_left - self.__nums[idx]),
            )

        self.__dp[idx][spaces_left] = result

        return self.__dp[idx][spaces_left]

    def solveWordWrap(self, nums: list[int], k: int) -> int:
        # Code here
        self.__nums = nums
        self.__k = k
        self.__dp = [[-1 for _ in range(k + 1)] for _ in range(len(nums))]

        return self.__solve_word_wrap_handler(1, k - nums[0])


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T: int = int(input())
    for i in range(T):
        n: int = int(input())
        nums: list[int] = list(map(int, input().split()))
        k: int = int(input())
        obj: Solution = Solution()
        ans: int = obj.solveWordWrap(nums, k)
        print(ans)


# } Driver Code Ends
