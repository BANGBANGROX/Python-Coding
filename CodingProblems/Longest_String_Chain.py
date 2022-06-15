from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        distance = {}

        for word in words:
            longest = 0
            for i in range(len(word)):
                nextWord = word[:i] + word[i+1:]
                longest = max(longest, distance.get(nextWord, 0))
            distance[word] = 1 + longest

        return max(distance.values())
