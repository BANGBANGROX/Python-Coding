from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = []
        b = []
        ans = 0
        count = dict()

        for i in range(n * n):
            x = i // n
            y = i % n
            val = x * 100 + y
            if img1[x][y] == 1:
                a.append(val)
            if img2[x][y] == 1:
                b.append(val)

        for x in a:
            for y in b:
                if count.get(x - y) == None:
                    count[x - y] = 0
                count[x - y] += 1

        for x in count:
            ans = max(ans, count[x])

        return ans


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        img1 = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                img1[i][j] = int(input())
        img2 = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                img2[i][j] = int(input())

        solution = Solution()
        print(solution.largestOverlap(img1, img2))
