class Solution:
    def __init__(self) -> None:
        self.__dp: list[int] = None
        self.__word_set: set[str] = None
        self.__s: str = None
        self.__n: int = 0

    def __min_extra_char_handler(self, idx: int) -> int:
        if idx >= self.__n:
            return 0

        if self.__dp[idx] != -1:
            return self.__dp[idx]

        result: int = self.__min_extra_char_handler(idx=idx + 1) + 1

        for i in range(idx, self.__n):
            substring: str = self.__s[idx : i + 1]
            if substring in self.__word_set:
                result = min(result, self.__min_extra_char_handler(idx=i + 1))

        self.__dp[idx] = result

        return self.__dp[idx]

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        self.__s = s
        self.__n = len(s)
        self.__dp = [-1] * self.__n
        self.__word_set = set(dictionary)

        return self.__min_extra_char_handler(idx=0)
