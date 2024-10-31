class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        columns = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)
        for r_index, row in enumerate(board):
            for c_index, num in enumerate(row):
                # iterating over every individual element
                if num == ".":
                    continue
                if num in columns[c_index]:
                    return False
                else:
                    columns[c_index].add(num)
                # columns are checked and updated
                if num in rows[r_index]:
                    return False
                else:
                    rows[r_index].add(num)
                # rows are checked and updated
                if num in grids[(c_index // 3), (r_index // 3)]:
                    return False
                else:
                    grids[((c_index // 3), (r_index // 3))].add(num)
                # each grid is now checked
        return True

"""
columns = {0: {5, 6}, 1: {3}}
rows = {0: {5, 3, 7}, 1: {6,}}
grids = {(0, 0): {5, 3}, (1,0): {7}}
r_index = 1
c_index = 0
"""

