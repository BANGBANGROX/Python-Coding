from typing import List


class Solution:
    def check(self, price, diff, k):
        next = price[0] + diff
        n = len(price)
        k -= 1

        for i in range(1, n):
            if price[i] >= next:
                k -= 1
                if k == 0:
                    break
                next = price[i] + diff

        return k == 0

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        l = 1
        r = 1e9

        while l <= r:
            mid = (l + r) // 2
            if self.check(price, mid, k):
                l = mid + 1
            else:
                r = mid - 1

        return l - 1
