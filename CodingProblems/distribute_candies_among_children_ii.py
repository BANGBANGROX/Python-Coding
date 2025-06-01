class Solution:
    def distribute_candies(self, n: int, limit: int) -> int:
        return self.__calc(x=n + 2) - 3 * self.__calc(x=n - limit + 1) + 3 * self.__calc(
            x=n - 2 * (limit + 1) + 2) - self.__calc(x=n - 3 * (limit + 1) + 2)

    def __calc(self, x: int) -> int:
        return x * (x - 1) // 2 if x > 0 else 0


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().distribute_candies(n=int(input()), limit=int(input())))
   