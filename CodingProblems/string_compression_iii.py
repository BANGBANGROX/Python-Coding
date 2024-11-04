class Solution:
    def compressedString(self, word: str) -> str:
        n: int = len(word)
        answer: list[str] = []
        i: int = 0

        while i < n:
            cnt: int = 1
            ch: str = word[i]
            while i + 1 < n and cnt < 9 and word[i] == word[i + 1]:
                cnt += 1
                i += 1
            answer.append(str(cnt))
            answer.append(ch)
            i += 1

        return "".join(answer)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().compressedString(word=input()))
