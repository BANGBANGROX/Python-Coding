def _build_palindromic_num(num: str, is_len_even: bool) -> int:
    reversed_num = num[::-1]
    palindromic_num_str = num + (reversed_num if is_len_even else reversed_num[1:])

    return int(palindromic_num_str)


def _are_all_digits_9(num: str) -> bool:
    for ch in num:
        if ord(ch) != ord("9"):
            return False

    return True


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        original_num = int(n)

        if original_num <= 10 or (
            original_num % 10 == 0 and n[0] == "1" and int(n[1:]) == 0
        ):
            return str(original_num - 1)

        if original_num == 11 or (
            original_num % 10 == 1 and n[0] == "1" and int(n[1:-1]) == 0
        ):
            return str(original_num - 2)

        if _are_all_digits_9(num=n):
            return str(original_num + 2)

        length = len(n)
        is_len_even = length % 2 == 0
        palindromic_root_str = (
            n[: length // 2] if is_len_even else n[: (length // 2 + 1)]
        )
        palindromic_root = int(palindromic_root_str)

        equal_palindromic_num = _build_palindromic_num(
            num=str(palindromic_root), is_len_even=is_len_even
        )
        equal_diff = abs(original_num - equal_palindromic_num)

        smaller_palindromic_num = _build_palindromic_num(
            num=str(palindromic_root - 1), is_len_even=is_len_even
        )
        smaller_diff = abs(original_num - smaller_palindromic_num)

        bigger_palindromic_num = _build_palindromic_num(
            num=str(palindromic_root + 1), is_len_even=is_len_even
        )
        bigger_diff = abs(original_num - bigger_palindromic_num)

        closest_palindromic_num = (
            smaller_palindromic_num
            if smaller_diff <= bigger_diff
            else bigger_palindromic_num
        )
        min_diff = min(smaller_diff, bigger_diff)

        if equal_diff != 0:
            if equal_diff < min_diff:
                closest_palindromic_num = equal_palindromic_num
            elif equal_diff == min_diff:
                closest_palindromic_num = min(
                    closest_palindromic_num, equal_palindromic_num
                )

        return str(closest_palindromic_num)


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().nearestPalindromic(n=input()))
