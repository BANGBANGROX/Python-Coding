from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        n = len(products)
        l = 0
        r = n - 1
        ans = [[] for _ in range(len(searchWord))]

        for i in range(len(searchWord)):
            if l > r:
                break
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            #current = []
            for j in range(l, r + 1):
                if j >= l + 3:
                    break
                ans[i].append(products[j])
            # ans.append(current)

        return ans
