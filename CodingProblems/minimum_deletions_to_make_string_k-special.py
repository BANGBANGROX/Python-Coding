from collections import Counter


class Solution:
    def minimum_deletions(self, word: str, k: int) -> int:
        answer: int = len(word)
        count: dict[str, int] = Counter(word)

        for (_, val1) in count.items():
            deletions: int = 0
            for (_, val2) in count.items():
                if val1 > val2:
                    deletions += val2
                elif val2 > val1 + k:
                    deletions += (val2 - val1 - k)
            answer = min(answer, deletions)

        return answer



if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().minimum_deletions(word=input(), k=int(input())))
