from collections import defaultdict


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        total_sum: int = sum(skill)
        n: int = len(skill)

        if ((total_sum * 2) % n) != 0:
            return -1

        target_sum: int = (total_sum * 2) // n
        count: defaultdict[int, int] = defaultdict(int)
        answer: int = 0

        for num in skill:
            count[num] += 1

        for i in range(n):
            if count[skill[i]] == 0:
                continue
            count[skill[i]] -= 1
            needed: int = target_sum - skill[i]
            if count[needed] == 0:
                return -1
            count[needed] -= 1
            answer += skill[i] * needed

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        skill: list[int] = [0] * n
        for i in range(n):
            skill[i] = int(input())

        print(Solution().dividePlayers(skill=skill))
