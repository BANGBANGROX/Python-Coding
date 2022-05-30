class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        temp = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -1 * (2 ** 31)
        sign = 1

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                ans |= (1 << i)

        ans *= sign

        if ans > INT_MAX:
            ans = INT_MAX

        if ans < INT_MIN:
            ans = INT_MIN

        return ans
