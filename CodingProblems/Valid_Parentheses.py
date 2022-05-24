from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if len(st) == 0:
                    return False
                poppedChar = st.pop()
                if (ch == ']' and poppedChar != '[') or (ch == '}' and poppedChar != '{') or (ch == ')' and poppedChar != '('):
                    return False

        return len(st) == 0
