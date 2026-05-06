class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_dict = {}
            for item in row:
                if item in row_dict and item != ".":
                    return False
                else:
                    row_dict[item] = True

        for col_index in range(9):
            column_dict = {}
            for row in board:
                if row[col_index] in column_dict and row[col_index] != ".":
                    return False
                else:
                    column_dict[row[col_index]] = True

        sub_matrix_list = [{} for _ in range(9)]
        for row_index in range(9):
            for column_index in range(9):
                sub_square_index = (row_index // 3) * 3 + (column_index // 3)
                if (
                    board[row_index][column_index] in sub_matrix_list[sub_square_index]
                    and board[row_index][column_index] != "."
                ):
                    return False
                else:
                    sub_matrix_list[sub_square_index][board[row_index][column_index]] = True

        return True
