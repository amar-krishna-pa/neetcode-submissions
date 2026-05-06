class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict_list = [{} for _ in range(9)]
        column_dict_list = [{} for _ in range(9)]
        sub_square_dict_list = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                sub_square_index = (i // 3) * 3 + (j // 3)

                if element in row_dict_list[i] and element != '.':
                    return False
                else:
                    row_dict_list[i][element] = True

                if element in column_dict_list[j] and element != '.':
                    return False
                else:
                    column_dict_list[j][element] = True
                
                if element in sub_square_dict_list[sub_square_index] and element != '.':
                    return False
                else:
                    sub_square_dict_list[sub_square_index][element] = True

        return True
