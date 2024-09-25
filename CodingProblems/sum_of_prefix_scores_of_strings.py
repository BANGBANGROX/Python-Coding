class _TrieNode:
    def __init__(self) -> None:
        self.children: list[_TrieNode] = [None] * 26
        self.end_cnt: int = 0


class Solution:
    def __init__(self) -> None:
        self.__root: _TrieNode = None

    def __insert_into_trie(self, word: str) -> None:
        p_crawl: _TrieNode = self.__root

        for ch in word:
            idx = ord(ch) - ord("a")
            if p_crawl.children[idx] is None:
                p_crawl.children[idx] = _TrieNode()
            p_crawl = p_crawl.children[idx]
            p_crawl.end_cnt += 1

    def __find_prefix_count(self, word: str) -> int:
        prefix_cnt: int = 0
        p_crawl: _TrieNode = self.__root

        for ch in word:
            idx = ord(ch) - ord("a")
            if p_crawl.children[idx] is None:
                return prefix_cnt
            p_crawl = p_crawl.children[idx]
            prefix_cnt += p_crawl.end_cnt

        return prefix_cnt

    def sumPrefixScores(self, words: list[str]) -> list[int]:
        n: int = len(words)
        answer: list[int] = [0] * n
        self.__root = _TrieNode()

        for word in words:
            self.__insert_into_trie(word=word)

        for i, word in enumerate(words):
            answer[i] = self.__find_prefix_count(word=word)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        words: list[str] = [None] * n

        for i in range(n):
            words[i] = input()

        print(Solution().sumPrefixScores(words=words))
