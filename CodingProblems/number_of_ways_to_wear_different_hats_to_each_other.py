MOD = 10 ** 9 + 7


class Solution:
    def __init__(self):
        self.__dp: list[list[int]] = []
        self.__people_hats_set: list[set[int]] = []
        self.__FULL_MASK: int = 0
        self.__MAX_HATS: int = 40
        self.__TOTAL_PEOPLE: int = 0

    def number_ways(self, hats: list[list[int]]) -> int:
        self.__people_hats_set = []
        self.__TOTAL_PEOPLE = len(hats)
        self.__FULL_MASK = (1 << self.__TOTAL_PEOPLE) - 1
        self.__dp = [[-1 for _ in range(self.__FULL_MASK + 1)] for _ in range(self.__MAX_HATS + 1)]

        for hat in hats:
            self.__people_hats_set.append(set(hat))

        return self.__number_ways_handler(current_hat=1, mask=0)

    def __number_ways_handler(self, current_hat: int, mask: int) -> int:
        if current_hat > self.__MAX_HATS:
            return 1 if mask == self.__FULL_MASK else 0

        if self.__dp[current_hat][mask] != -1:
            return self.__dp[current_hat][mask]

        total_ways = self.__number_ways_handler(current_hat + 1, mask)

        for i in range(self.__TOTAL_PEOPLE):
            if (mask & (1 << i)) > 0 or current_hat not in self.__people_hats_set[i]:
                continue
            total_ways = (total_ways + self.__number_ways_handler(current_hat=current_hat + 1,
                                                                  mask=mask | (1 << i))) % MOD

        self.__dp[current_hat][mask] = total_ways

        return total_ways


if __name__ == '__main__':
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        hats: list[list[int]] = []
        for i in range(n):
            hats.append([])
            current_hats_cnt: int = int(input())
            for j in range(current_hats_cnt):
                hats[i].append(int(input()))

        print(Solution().number_ways(hats=hats))
