class Solution:
    def minEnd(self, n: int, x: int) -> int:
        MAX_BITS: int = 64
        bit_counter: int = 0
        answer: int = 0

        n -= 1

        for i in range(MAX_BITS):
            current_bit: int = 0
            if (x & (1 << i)) > 0:
                current_bit = 1
            else:
                if (n & (1 << bit_counter)) > 0:
                    current_bit = 1
                bit_counter += 1
            if current_bit == 1:
                answer |= 1 << i

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().minEnd(n=int(input()), x=int(input())))
