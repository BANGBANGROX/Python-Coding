class Solution:
    def possible_string_count(self, word: str, k: int) -> int:
        run_lengths: list[int] = []
        current_length: int = 0
        last_char: str = '#'
        mod: int = 10 ** 9 + 7
        total_possible_words: int = 1

        for ch in word:
            if ch == last_char:
                current_length += 1
            else:
                if current_length > 0:
                    run_lengths.append(current_length)
                current_length = 1
                last_char = ch

        if current_length > 0:
            run_lengths.append(current_length)

        for run_length in run_lengths:
            total_possible_words = (total_possible_words * run_length) % mod

        if len(run_lengths) >= k:
            return total_possible_words

        count: list[int] = [0] * k
        prefix_sum: list[int] = [0] * k
        achievable_length: int = run_lengths[0]

        for i in range(1, min(run_lengths[0] + 1, k)):
            count[i] = 1

        for i in range(1, k):
            prefix_sum[i] = (prefix_sum[i - 1] + count[i]) % mod

        for i in range(1, len(run_lengths)):
            starting_point: int = i + 1
            run_length: int = run_lengths[i]
            count = [0] * k
            achievable_length += run_length

            for j in range(starting_point, min(achievable_length + 1, k)):
                count[j] = (prefix_sum[j - 1] - (prefix_sum[j - run_length - 1] if j - run_length - 1 >= 0 else 0)
                            + mod) % mod

            for j in range(1, k):
                prefix_sum[j] = (prefix_sum[j - 1] + count[j]) % mod

        return (total_possible_words - prefix_sum[k - 1] + mod) % mod


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().possible_string_count(input(), int(input())))
