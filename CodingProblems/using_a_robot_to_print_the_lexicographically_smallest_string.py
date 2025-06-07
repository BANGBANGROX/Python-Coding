from collections import Counter


class Solution:
    def robot_with_string(self, s: str) -> str:
        count: Counter[str] = Counter(s)
        answer: list[str] = []
        stack: list[str] = []
        min_character: str = "a"

        for ch in s:
            stack.append(ch)
            count[ch] -= 1
            while min_character != "z" and count[min_character] == 0:
                min_character = chr(ord(min_character) + 1)
            while len(stack) > 0 and stack[-1] <= min_character:
                answer.append(stack.pop())

        return "".join(answer)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().robot_with_string(s=input()))