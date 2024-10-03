class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in range(0, 9):
                currNum = row[i]
                if currNum != ".":
                    if currNum in seen:
                        return False
                    else:
                        seen.add(currNum)
        # we've verified each row is valid.

        for column in range(0, 9):
            valid_column = self.is_valid_column(board, column)
            # if we have an invalid column, we'd get false, so it becomes true, then we return false
            if not valid_column:
                return False
        
        # we've validated each column is valid.
        grid_check_locs = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
            ]
        for i in range(0, 9):
            row, column = grid_check_locs[i]
            valid_grid = self.is_valid_3_by_3(board, row, column)
            if not valid_grid:
                return False
        # 3 by 3 grid has been validated.
        return True

# row = 0
# column = 0
# i = 1
# j = 0
# seen = {5, 3, }

    def is_valid_3_by_3(self, board, row, column):
        seen = set()
        for i in range(0, 3):
            for j in range(0, 3):
                currNum = board[row + i][column + j]
                if currNum != ".":
                    if currNum in seen:
                        return False
                    else:
                        seen.add(currNum)
        return True

    def is_valid_column(self, board, column):
            set1 = set()
            for row in range(0, 9):
                currNum = board[row][column]
                if currNum != ".":
                    if currNum in set1:
                        return False
                    else:
                        set1.add(currNum)
            return True
            # now we've validated this column

                    
            # column = 1
            # row = 0
            # set1 = {3, 9}

