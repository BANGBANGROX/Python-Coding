from typing import List


class Solution:
    def __init__(self):
        self.n = None
        self.dp = None
        self.graph = None

    def _vertex_cover_handler(self, mask : int) -> int:
        if self.dp[mask] != -1:
            return self.dp[mask]

        can_add = False
        result = int(1e9)

        for i in range(self.n):
            if (mask & (1 << i)) == 0:
                for child in self.graph[i]:
                    if (mask & (1 << child)) == 0:
                        can_add = True
                        break
                if can_add:
                    break

        if not can_add:
            return bin(mask).count("1")

        for i in range(n):
            if (mask & (1 << i)) == 0:
                result = min(result, self._vertex_cover_handler(mask | (1 << i)))

        self.dp[mask] = result

        return result

    def vertexCover(self, n: int, edges: List[List[int]]) -> int:
        self.n = n
        self.dp = [-1] * (1 << n)
        self.graph = []

        for i in range(n):
            self.graph.append([])

        for edge in edges:
            self.graph[edge[0] - 1].append(edge[1] - 1)
            self.graph[edge[1] - 1].append(edge[0] - 1)

        return self._vertex_cover_handler(0)



# code here


# {
# Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        m = int(input())

        edges = IntMatrix().Input(m, m)

        obj = Solution()
        res = obj.vertexCover(n, edges)

        print(res)

# } Driver Code Ends