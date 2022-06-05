class Solution(object):
    def check(self, row: int, col: int, state: List[str], n: int) -> bool:
        startRow = row - 1
        displacement = 1

        while startRow >= 0:
            if state[startRow][col] == 'Q' or (col >= displacement and state[startRow][col - displacement] == 'Q') or (col + displacement < n and state[startRow][col + displacement] == 'Q'):
                return False
            startRow -= 1
            displacement += 1

        return True

    def fillQueens(self, row: int, current, n: int):
        if row == n:
            self.ans += 1
            return

        # Find a square for the queen on the current row
        for i in range(n):
            if self.check(row, i, current, n):
                current[row][i] = 'Q'
                self.fillQueens(row + 1, current, n)
                current[row][i] = '.'

    def totalNQueens(self, n: int):
        self.ans = 0
        current = [['.' for _ in range(n)] for __ in range(n)]

        self.fillQueens(0, current, n)

        return self.ans
