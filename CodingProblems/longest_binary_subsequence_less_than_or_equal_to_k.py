from math import log2


class Solution:
    def longest_subsequence(self, s: str, k: int) -> int:
        overall_bits_needed: int = int(log2(k)) + 1
        n: int = len(s)
        current_bits: int = 0
        current_num: int = 0

        for i in range(n):
            last_idx: int = n - i - 1
            if s[last_idx] == '1':
                if current_bits < overall_bits_needed and current_num + (1 << i) <= k:
                    current_num += (1 << i)
                    current_bits += 1
            else:
                current_bits += 1

        return current_bits


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().longest_subsequence(s=input(), k=int(input())))
