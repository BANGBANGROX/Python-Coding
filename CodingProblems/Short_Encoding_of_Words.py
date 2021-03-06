from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)

        for word in words:
            for i in range(1, len(word)):
                good.discard(word[i:])

        return (sum(len(word) + 1 for word in good))
