class _TrieNode:
    def __init__(self) -> None:
        self.children: list[_TrieNode] = [None] * 10


class Solution:
    def __init__(self) -> None:
        self.__root: _TrieNode = None

    def __add_to_trie(self, num: str) -> None:
        p_crawl: _TrieNode = self.__root

        for dig in num:
            idx: int = ord(dig) - ord("0")
            if p_crawl.children[idx] is None:
                p_crawl.children[idx] = _TrieNode()
            p_crawl = p_crawl.children[idx]

    def __find_matching_length(self, num: str) -> int:
        p_crawl: _TrieNode = self.__root

        for i, dig in enumerate(num):
            idx: int = ord(dig) - ord("0")
            if p_crawl.children[idx] is not None:
                p_crawl = p_crawl.children[idx]
            else:
                return i

        return len(num)

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        answer: int = 0
        self.__root = _TrieNode()

        for num in arr1:
            self.__add_to_trie(num=str(num))

        for num in arr2:
            answer = max(answer, self.__find_matching_length(num=str(num)))

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        arr1: list[int] = [0] * m
        for i in range(m):
            arr1[i] = int(input())
        n: int = int(input())
        arr2: list[int] = [0] * n
        for i in range(n):
            arr2[i] = int(input())

        print(Solution().longestCommonPrefix(arr1=arr1, arr2=arr2))
