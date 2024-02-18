from typing import List


class Solution:
    class TrieNode:
        def __init__(self):
            self.children = dict()
            self.cnt = 0

    def count_prefix_suffix_pairs(self, words_list: List[str]) -> int:
        root = self.TrieNode()
        answer = 0

        for word in words_list:
            length = len(word)
            p_crawl = root
            for i in range(0, length):
                first_and_last_char = f"{word[i]}|{word[length - i - 1]}"
                if p_crawl.children.get(first_and_last_char) is None:
                    p_crawl.children[first_and_last_char] = self.TrieNode()
                p_crawl = p_crawl.children[first_and_last_char]
                answer += p_crawl.cnt
            p_crawl.cnt += 1

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        words = []
        for i in range(n):
            words.append(input())

        solution = Solution()
        print(solution.count_prefix_suffix_pairs(words))
