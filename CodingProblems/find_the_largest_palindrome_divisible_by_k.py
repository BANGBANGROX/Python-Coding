def _is_num_divisible_by_7(num: str) -> bool:
    rem = 0

    for dig in num:
        rem = (rem * 10 + (ord(dig) - ord("0"))) % 7

    return rem == 0


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            if k in [1, 3, 9]:
                return "9"
            if k in [2, 4, 8]:
                return "8"
            if k == 5:
                return "5"
            if k == 6:
                return "6"
            if k == 7:
                return "7"
            return "-1"

        if n == 2:
            if k in [1, 3, 9]:
                return "99"
            if k in [2, 4, 8]:
                return "88"
            if k == 5:
                return "55"
            if k == 6:
                return "66"
            if k == 7:
                return "77"
            return "-1"

        if n == 3:
            if k in [1, 3, 9]:
                return "999"
            if k == 2:
                return "898"
            if k in [4, 8]:
                return "888"
            if k == 5:
                return "595"
            if k == 6:
                return "888"
            if k == 7:
                return "959"
            return "-1"

        if n == 4:
            if k in [1, 3, 9]:
                return "9999"
            if k == 2:
                return "8998"
            if k in [4, 8]:
                return "8888"
            if k == 5:
                return "5995"
            if k == 6:
                return "8778"
            if k == 7:
                return "9779"
            return "-1"

        # n > 4
        answer = ["9"] * n

        if k in [1, 3, 9]:
            return "".join(answer)

        if k == 2:
            answer[0] = answer[-1] = "8"
            return "".join(answer)

        if k == 4:
            answer[0] = answer[-1] = answer[1] = answer[-2] = "8"
            return "".join(answer)

        if k == 5:
            answer[0] = answer[-1] = "5"
            return "".join(answer)

        if k == 6:
            total_sum = 9 * n - 2
            answer[0] = answer[-1] = "8"

            if total_sum % 3 != 0:
                if n % 2 == 1:
                    answer[n // 2] = "8"
                else:
                    answer[(n // 2)] = answer[(n // 2) - 1] = "7"

            return "".join(answer)

        if k == 7:
            for dig in range(9, -1, -1):
                if n % 2 == 1:
                    answer[(n // 2)] = str(dig)
                else:
                    answer[(n // 2)] = answer[(n // 2) - 1] = str(dig)
                if _is_num_divisible_by_7(num=answer):
                    return "".join(answer)

        if k == 8:
            answer[0] = answer[-1] = answer[1] = answer[-2] = answer[2] = answer[-3] = (
                "8"
            )
            return "".join(answer)

        return "-1"


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().largestPalindrome(n=int(input()), k=int(input())))
