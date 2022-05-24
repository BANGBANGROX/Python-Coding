class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        opening = 0
        closing = 0
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                opening += 1
            else:
                closing += 1
            if opening == closing:
                maxLength = max(maxLength, 2 * opening)
            elif closing > opening:
                closing = opening = 0

        opening = closing = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                opening += 1
            else:
                closing += 1
            if opening == closing:
                maxLength = max(maxLength, 2 * opening)
            elif closing < opening:
                closing = opening = 0

        return maxLength
