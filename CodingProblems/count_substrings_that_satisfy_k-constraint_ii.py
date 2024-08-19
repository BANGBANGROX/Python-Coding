from typing import List


class Solution:
    def _lower_bound(self, nums: list[int], left: int, right: int, key: int) -> int:
        result = right + 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= key:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def countKConstraintSubstrings(
        self, s: str, k: int, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        first_index = [0] * n
        length_prefix_sum = [0] * n
        answer = []
        left = 0
        right = 0
        zeroes_cnt = 0
        ones_cnt = 0

        for right in range(n):
            if ord(s[right]) == ord("0"):
                zeroes_cnt += 1
            else:
                ones_cnt += 1
            while ones_cnt > k and zeroes_cnt > k:
                if ord(s[left]) == ord("0"):
                    zeroes_cnt -= 1
                else:
                    ones_cnt -= 1
                left += 1
            first_index[right] = left
            length_prefix_sum[right] = (
                right - left + 1 + (length_prefix_sum[right - 1] if right > 0 else 0)
            )

        for left_end, right_end in queries:
            idx = self._lower_bound(
                nums=first_index, left=left_end, right=right_end, key=left_end
            )
            result = length_prefix_sum[right_end] - (
                length_prefix_sum[idx - 1] if idx > 0 else 0
            )
            idx -= left_end
            result += idx * (idx + 1) // 2
            answer.append(result)

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        s = input()
        k = int(input())
        q = int(input())
        queries = [[0 for _ in range(2)] for _ in range(q)]
        for i in range(q):
            queries[i][0] = int(input())
            queries[i][1] = int(input())

        print(Solution().countKConstraintSubstrings(s=s, k=k, queries=queries))
