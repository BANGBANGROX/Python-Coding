from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coin_avb = defaultdict(int)

        for bill in bills:
            if bill > 5:
                change = bill - 5
                # change can be 5 or 15
                if change == 5:
                    if coin_avb[5] == 0:
                        return False
                    coin_avb[5] -= 1
                elif change == 15:
                    if coin_avb[10] > 0 and coin_avb[5] > 0:
                        coin_avb[10] -= 1
                        coin_avb[5] -= 1
                    elif coin_avb[5] > 2:
                        coin_avb[5] -= 3
                    else:
                        return False
            coin_avb[bill] += 1

        return True


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        bills = List()

        for _ in range(n):
            bills.append(int(input()))

        print(Solution().lemonadeChange(bills=bills))
