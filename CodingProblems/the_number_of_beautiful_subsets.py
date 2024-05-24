from typing import List
from collections import OrderedDict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        remainder_nums = {}
        answer = 1

        nums.sort()

        for num in nums:
            if remainder_nums.get(num % k) is None:
                remainder_nums[num % k] = []
            remainder_nums[num % k].append(num)

        for (_, current_nums) in remainder_nums.items():
            count = OrderedDict()
            for num in current_nums:
                if count.get(num) is None:
                    count[num] = 0
                count[num] += 1
            prev_not_taken = 1
            prev_taken = 0
            last_element = -1000000
            for (num, cnt) in count.items():
                total_subsets = (1 << cnt) - 1
                curr_not_taken = prev_taken + prev_not_taken
                if last_element + k == num:
                    curr_taken = prev_not_taken * total_subsets
                else:
                    curr_taken = (prev_taken + prev_not_taken) * total_subsets
                last_element = num
                prev_not_taken = curr_not_taken
                prev_taken = curr_taken
            answer *= (prev_taken + prev_not_taken)

        return answer - 1
