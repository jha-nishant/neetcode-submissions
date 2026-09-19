class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = [set() for i in range(9)]
        colList = [set() for i in range(9)]
        boxList = [set() for i in range(9)]
        # for i in range(9):
        #    rowList[i] = set()
        #    colList[i] = set()
        #    boxList[i] = set()

        isValid = True
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                # i is row, j is col
                if cell != ".":
                    # add to row
                    row = rowList[i]
                    if cell in row:
                        isValid = False
                    row.add(cell)
                    rowList[i] = row
                    print(isValid)

                    # add to col
                    col = colList[j]
                    if cell in col:
                        isValid = False
                    col.add(cell)
                    colList[j] = col
                    print(isValid)

                    # add to box
                    r = int(i / 3)
                    c = int(j / 3)

                    index = 3 * r + c
                    box = boxList[index]
                    if cell in box:
                        isValid = False
                    box.add(cell)
                    boxList[index] = box
        
        return isValid

                
