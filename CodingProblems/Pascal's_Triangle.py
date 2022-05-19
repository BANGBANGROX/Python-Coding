from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(0, numRows):
            current = []
            for j in range(0, i + 1):
                if j == 0 or j >= len(ans[i - 1]) or i == 0:
                    current.append(1)
                else:
                    current.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(current)

        return ans
