from typing import List


class Solution:
    def __init__(self):
        self.dp: list[list[int]] = []
        self.requirements_map: dict[int, int] = {}

    def __number_of_permutations_handler(self, nums_left: int, current_inversions: int) -> int:
        if nums_left == 1:
            return 1 if current_inversions == 0 else 0

        if current_inversions < 0 or (
                nums_left in self.requirements_map and self.requirements_map[nums_left] != current_inversions):
            return 0

        if self.dp[nums_left][current_inversions] != -1:
            return self.dp[nums_left][current_inversions]

        MOD = 1e9 + 7
        result = 0

        for i in range(1, nums_left + 1):
            inversions_used = nums_left - i
            result = (result + self.__number_of_permutations_handler(nums_left=nums_left - 1,

                                                                     current_inversions=current_inversions - inversions_used)) % MOD

        self.dp[nums_left][current_inversions] = int(result)

        return self.dp[nums_left][current_inversions]

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MAX_CNT = 405
        self.dp = [[-1 for _ in range(MAX_CNT)] for __ in range(n + 1)]
        self.requirements_map = {requirement[0] + 1: requirement[1] for requirement in requirements}

        return self.__number_of_permutations_handler(nums_left=n, current_inversions=self.requirements_map[n])


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        m = int(input())
        requirements = [[0 for _ in range(2)] for __ in range(m)]
        for i in range(m):
            requirements[i][0] = int(input())
            requirements[i][1] = int(input())

        print(Solution().numberOfPermutations(n=n, requirements=requirements))