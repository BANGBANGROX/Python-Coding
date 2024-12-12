# User function Template for python3
class Solution:
    def __init__(self):
        self.__outgoing: list[int] | None = None
        self.__visited: list[int] | None = None
        self.__weights: list[int] | None = None
        self.__min_weight: int = 0

    def __find(self, node: int) -> int:
        if self.__outgoing[node] == 0:
            return node

        self.__min_weight = min(self.__min_weight, self.__weights[node])

        return self.__find(self.__outgoing[node])

    def solve(self, n: int, p: int, a: list[int], b: list[int], d: list[int]) -> list[list[int]]:
        self.__outgoing = [0] * (n + 1)
        self.__visited = [False] * (n + 1)
        self.__weights = [0] * (n + 1)
        incoming: list[int] = [0] * (n + 1)
        answer: list[list[int]] = []

        for i in range(p):
            self.__outgoing[a[i]] = b[i]
            incoming[b[i]] = a[i]
            self.__weights[a[i]] = d[i]

        for i in range(1, n + 1):
            if not self.__visited[i] and incoming[i] == 0:
                self.__min_weight = 10**9
                endpoint = self.__find(i)
                if i != endpoint:
                    answer.append([i, endpoint, self.__min_weight])

        return answer


# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n, p = map(int, input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x, y, z = map(int, input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)

        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]))

# } Driver Code Ends