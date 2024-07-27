def _compute_lps(s: str) -> list[int]:
    n = len(s)
    lps = [0] * n
    i = 1
    match_len = 0

    while i < n:
        if s[i] == s[match_len]:
            match_len += 1
            lps[i] = match_len
            i += 1
        else:
            if match_len > 0:
                match_len = lps[match_len - 1]
            else:
                i += 1

    return lps


class Solution:
    def __init__(self) -> None:
        self.__n: int = 0
        self.__s1: str = None
        self.__s2: str = None
        self.__evil: str = None
        self.__dp: list[list[list[list[int]]]] = []
        self.__lps: list[int] = []

    def __find_good_strings_handler(
        self,
        idx: int,
        evil_length: int,
        left_bound_passed: bool,
        right_bound_passed: bool,
    ) -> int:
        if evil_length >= len(self.__evil):
            return 0

        if idx >= self.__n:
            return 1

        if self.__dp[idx][evil_length][left_bound_passed][right_bound_passed] != -1:
            return self.__dp[idx][evil_length][left_bound_passed][right_bound_passed]

        MOD = 10**9 + 7
        result = 0
        left_bound = ord(self.__s1[idx]) if left_bound_passed else ord("a")
        right_bound = ord(self.__s2[idx]) if right_bound_passed else ord("z")

        for ch in range(left_bound, right_bound + 1):
            j = evil_length
            while j > 0 and ord(self.__evil[j]) != ch:
                j = self.__lps[j - 1]
            if ord(self.__evil[j]) == ch:
                j += 1
            result = (
                result
                + self.__find_good_strings_handler(
                    idx=idx + 1,
                    evil_length=j,
                    left_bound_passed=left_bound_passed and (ch == left_bound),
                    right_bound_passed=right_bound_passed and (ch == right_bound),
                )
            ) % MOD

        self.__dp[idx][evil_length][left_bound_passed][right_bound_passed] = result

        return result

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        self.__n = n
        self.__s1 = s1
        self.__s2 = s2
        self.__evil = evil
        self.__lps = _compute_lps(evil)
        self.__dp = [
            [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(len(evil))]
            for _ in range(n)
        ]

        return self.__find_good_strings_handler(
            idx=0, evil_length=0, left_bound_passed=True, right_bound_passed=True
        )


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(
            Solution().findGoodStrings(
                n=int(input()), s1=input(), s2=input(), evil=input()
            )
        )
