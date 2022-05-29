from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        occ = [[False] for _ in range(26)] * n
        ans = -1

        for i in range(n):
            for ch in words[i]:
                occ[i][ord(ch) - ord('a')] = True

        for i in range(n):
            for j in range(i + 1, n):
                isSame = False
                for k in range(26):
                    if occ[i][k] and occ[j][k]:
                        isSame = True
                        break
                if not isSame:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
