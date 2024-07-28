from collections import deque


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        n = len(s)

        for req_zeroes_cnt in range(1, int(n**0.5) + 1):
            ones_cnt = 0
            last_zero_index = -1
            zero_indices = deque()
            for right in range(n):
                if s[right] == "0":
                    zero_indices.append(right)
                    while len(zero_indices) > req_zeroes_cnt:
                        ones_cnt -= zero_indices[0] - last_zero_index - 1
                        last_zero_index = zero_indices.popleft()
                else:
                    ones_cnt += 1
                if (
                    len(zero_indices) == req_zeroes_cnt
                    and ones_cnt >= req_zeroes_cnt**2
                ):
                    answer += min(
                        zero_indices[0] - last_zero_index,
                        ones_cnt - req_zeroes_cnt * req_zeroes_cnt + 1,
                    )

        idx = 0

        while idx < n:
            if s[idx] == "1":
                ones_cnt = 0
                while idx < n and s[idx] == "1":
                    ones_cnt += 1
                    idx += 1
                answer += ones_cnt * (ones_cnt + 1) // 2
            else:
                idx += 1

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().numberOfSubstrings(s=input()))
