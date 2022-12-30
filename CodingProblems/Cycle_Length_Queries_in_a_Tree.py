from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []

        for query in queries:
            a = query[0]
            b = query[1]
            result = 1
            while a != b:
                if a < b:
                    t = a
                    a = b
                    b = t
                a //= 2
                result += 1
            ans.append(result)

        return ans


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n = int(input())
        queries = []
        for i in range(n):
            a = int(input())
            b = int(input())
            queries.append([a, b])

        solution = Solution()
        print(solution.cycleLengthQueries(n, queries))
