class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1: list[str] = sentence1.split(" ")
        words2: list[str] = sentence2.split(" ")
        m: int = len(words1)
        n: int = len(words2)

        if m > n:
            return self.areSentencesSimilar(sentence1=sentence2, sentence2=sentence1)

        i: int = 0

        while i < m and words1[i] == words2[i]:
            i += 1

        while i < m and words1[i] == words2[n - m + i]:
            i += 1

        return i == m


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().areSentencesSimilar(sentence1=input(), sentence2=input()))
