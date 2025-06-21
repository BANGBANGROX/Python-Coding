_MAX_VALUE = 10 ** 5 + 5
_MOD: int = 10 ** 9 + 7
_FACTORIAL: list[int] = [0] * _MAX_VALUE
_INVERSE_FACTORIAL: list[int] = [0] * _MAX_VALUE


def _init() -> None:
    if _FACTORIAL[0] == 1:
        return

    _FACTORIAL[0] = _INVERSE_FACTORIAL[0] = 1

    for i in range(1, _MAX_VALUE):
        _FACTORIAL[i] = (_FACTORIAL[i - 1] * i) % _MOD
        _INVERSE_FACTORIAL[i] = _calculate_inverse(_FACTORIAL[i])


def _calculate_power(a: int, b: int) -> int:
    result: int = 1

    while b > 0:
        if (b & 1) > 0:
            result = (result * a) % _MOD
            b -= 1
        a = (a * a) % _MOD
        b >>= 1

    return result


def _calculate_inverse(val: int) -> int:
    return _calculate_power(a=val, b=_MOD - 2)


def _calculate_ncr(n: int, r: int) -> int:
    if n < r:
        return 0

    return (_FACTORIAL[n] * (_INVERSE_FACTORIAL[r] * _INVERSE_FACTORIAL[n - r]) % _MOD) % _MOD


class Solution:
    def __init__(self) -> None:
        _init()

    def count_good_arrays(self, n: int, m: int, k: int) -> int:
        return (_calculate_ncr(n - 1, k) * (m * _calculate_power(m - 1, n - k - 1)) % _MOD) % _MOD


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().count_good_arrays(n=int(input()), m=int(input()), k=int(input())))
