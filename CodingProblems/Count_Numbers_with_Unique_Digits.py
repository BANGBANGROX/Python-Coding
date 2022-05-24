class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 10

        ans = 10
        add = 81
        mul = 8

        for i in range(2, n + 1):
            ans += add
            add *= mul
            mul -= 1

        return ans
