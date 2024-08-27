from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.__MAX_NUM_LENGTH = 8

    def __add_leading_zeroes(self, num: int) -> str:
        result = str(num)
        curr_len = len(result)

        for _ in range(self.__MAX_NUM_LENGTH - curr_len):
            result = "0" + result

        return result

    def __generate_all_possible_nums(self, num: int) -> set[str]:
        result = set[str]()
        num_list = list(self.__add_leading_zeroes(num=num))

        for i in range(self.__MAX_NUM_LENGTH):
            for j in range(i + 1, self.__MAX_NUM_LENGTH):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                result.add("".join(num_list))
                for next_i in range(self.__MAX_NUM_LENGTH):
                    for next_j in range(next_i + 1, self.__MAX_NUM_LENGTH):
                        num_list[next_i], num_list[next_j] = (
                            num_list[next_j],
                            num_list[next_i],
                        )
                        result.add("".join(num_list))
                        num_list[next_i], num_list[next_j] = (
                            num_list[next_j],
                            num_list[next_i],
                        )
                num_list[i], num_list[j] = num_list[j], num_list[i]

        return result

    def countPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        answer = 0

        for num in nums:
            all_poss_nums = self.__generate_all_possible_nums(num=num)
            num_str = self.__add_leading_zeroes(num=num)
            for poss_num in all_poss_nums:
                if count.get(poss_num) is not None:
                    answer += count[poss_num]
            count[num_str] += 1

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = List[int]()
        for _ in range(n):
            nums.append(int(input()))

        print(Solution().countPairs(nums=nums))
