from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.maxIndex = 0


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for i, word in enumerate(words):
            newWord = word + '#' + word
            for j in range(len(word)):
                current = self.root
                for k in range(j, len(newWord)):
                    c = newWord[k]
                    if c not in current.children:
                        current.children[c] = TrieNode()
                    current = current.children[c]
                    current.maxIndex = i

    def f(self, prefix: str, suffix: str) -> int:
        current = self.root
        searchWord = suffix + '#' + prefix

        for c in searchWord:
            if c not in current.children:
                return -1
            current = current.children[c]

        return current.maxIndex
