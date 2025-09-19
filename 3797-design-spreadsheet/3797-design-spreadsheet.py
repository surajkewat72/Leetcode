class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid = [[0] * self.cols for _ in range(rows)]
    
    def _cell_to_index(self, cell: str):
        col = ord(cell[0]) - ord('A') 
        row = int(cell[1:]) - 1       
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._cell_to_index(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._cell_to_index(cell)
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split('+')

        def get_val(token):
            token = token.strip()
            if token[0].isalpha(): 
                row, col = self._cell_to_index(token)
                return self.grid[row][col]
            else:  
                return int(token)

        return get_val(x) + get_val(y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
