from ast import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9
        rowsResult = True
        colsResult = True
        sqauresResult = True

        # Check rows
        for i in range(0, m):
            count = {}
            for j in range(0, m):
                if board[i][j] == "":
                    continue
                if count.get(board[i][j]) == None:
                    count[board[i][j]] = 0
                count[board[i][j]] += 1
                if count[board[i][j]] > 1:
                    rowsResult = False
                    break
            if rowsResult == False:
                break

        if rowsResult == False:
            return False

        # Check cols
        for j in range(0, m):
            count = {}
            for i in range(0, m):
                if board[i][j] == "":
                    continue
                if count.get(board[i][j]) == None:
                    count[board[i][j]] = 0
                count[board[i][j]] += 1
                if count[board[i][j]] > 1:
                    colsResult = False
                    break
            if colsResult == False:
                break

        if colsResult == False:
            return False

        # Check 3x3 squares
        for j in range(0, m, 3):
            for i in range(0, m, 3):
                count = {}
                for k in range(j, j + 3):
                    for l in range(i, i + 3):
                        if board[k][l] == "":
                            continue
                        if count.get(board[k][l]) == None:
                            count[board[k][l]] = 0
                        count[board[k][l]] += 1
                        if count[board[k][l]] > 1:
                            sqauresResult = False
                            break
                    if sqauresResult == False:
                        break
                if sqauresResult == False:
                    break
            if sqauresResult == False:
                break

        return sqauresResult
