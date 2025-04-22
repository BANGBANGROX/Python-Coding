_MAX_VALUE: int = 10010
_MAX_PRIME_FACTORS: int = 15
_prime_factorization: list[list[int]] = [[] for _ in range(_MAX_VALUE)]
_dp: list[list[int]] = [[0 for _ in range(_MAX_PRIME_FACTORS + 1)]
                                      for _ in range(_MAX_VALUE + _MAX_PRIME_FACTORS)]
_MOD: int = 10 ** 9 + 7

def _init():
    smallest_prime_factor: list[int] = [0 for _ in range(_MAX_VALUE)]

    for i in range(2, _MAX_VALUE):
        if smallest_prime_factor[i] == 0:
            for j in range(i, _MAX_VALUE, i):
                if smallest_prime_factor[j] == 0:
                    smallest_prime_factor[j] = i

    for i in range(2, _MAX_VALUE):
        current_value: int = i
        while current_value > 1:
            prime_factor: int = smallest_prime_factor[current_value]
            cnt: int = 0
            while current_value % prime_factor == 0:
                cnt += 1
                current_value //= prime_factor
            _prime_factorization[i].append(cnt)

    _dp[0][0] = 1

    for i in range(1, _MAX_VALUE + _MAX_PRIME_FACTORS):
        _dp[i][0] = 1
        for j in range(1, min(i, _MAX_PRIME_FACTORS) + 1):
            _dp[i][j] = (_dp[i - 1][j] + _dp[i - 1][j - 1]) % _MOD

class Solution:
    def __init__(self):
        if _dp[0][0] == 1:
            return

        _init()

    def idealArrays(self, n: int, max_value: int) -> int:
        answer: int = 0

        for i in range(1, max_value + 1):
            mul: int = 1
            for prime in _prime_factorization[i]:
                mul = (mul * _dp[n + prime - 1][prime]) % _MOD
            answer = (answer + mul) % _MOD

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        max_value: int = int(input())

        print(Solution().idealArrays(n=n, max_value=max_value))
