class Solution:
    def __init__(self) -> None:
        self.__n: int = 0

    def __count_nums_with_prefix(self, first: int, second: int) -> int:
        cnt: int = 0

        while first <= self.__n:
            cnt += min(self.__n + 1, second) - first
            first *= 10
            second *= 10

        return cnt

    def findKthNumber(self, n: int, k: int) -> int:
        self.__n = n
        answer = 1
        k -= 1

        while k > 0:
            steps: int = self.__count_nums_with_prefix(first=answer, second=answer + 1)
            if steps <= k:
                k -= steps
                answer += 1
            else:
                k -= 1
                answer *= 10

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().findKthNumber(n=int(input()), k=int(input())))
