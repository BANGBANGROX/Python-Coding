class Solution:
    def __init__(self) -> None:
        self.__s1: str = None
        self.__s2: str = None
        self.__dp: list[list[int]] = None

    def __edit_distance_handler(self, i: int, j: int) -> int:
        if i == 0 or j == 0:
            return i + j

        if self.__dp[i][j] != -1:
            return self.__dp[i][j]

        if self.__s1[i - 1] == self.__s2[j - 1]:
            self.__dp[i][j] = self.__edit_distance_handler(i - 1, j - 1)
        else:
            self.__dp[i][j] = (
                min(
                    self.__edit_distance_handler(i - 1, j),
                    self.__edit_distance_handler(i, j - 1),
                    self.__edit_distance_handler(i - 1, j - 1),
                )
                + 1
            )

        return self.__dp[i][j]

    def editDistance(self, str1: str, str2: str) -> int:
        # Code here
        self.__s1 = str1
        self.__s2 = str2
        self.__dp = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

        return self.__edit_distance_handler(len(str1), len(str2))


# {
# Driver Code Starts
if __name__ == "__main__":
    T: int = int(input())
    for i in range(T):
        s, t = input().split()
        ob: Solution = Solution()
        ans: int = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends
