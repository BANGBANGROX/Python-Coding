import math
from collections import defaultdict


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count: dict[int, int] = defaultdict(int)
        answer: int = 0

        for val in answers:
            count[val] += 1

        for (val, cnt) in count.items():
            answer += int(math.ceil(cnt / (val + 1))) * (val + 1)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        answers: list[int] = [int(input()) for _ in range(n)]

        print(Solution().numRabbits(answers=answers))