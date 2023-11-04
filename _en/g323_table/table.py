"""Create Table class and display the table in the command line interface.

|------|------|------|
|      | Col0 | Col1 |
|------|------|------|
| Row0 |   1  |  23  |
|------|------|------|
| Row1 |  13  |   9  |
|------|------|------|

Some Useful Information:
1. The program creates a Table class including attributes like row_headers, col_headers, row_count,
   col_count, data, and methods like fill(), random(), clear(), del_row(), del_col().
2. table objects can be displayed as a table with dividing lines in the command line interface.
   characters of different widths can be used in the table. The width of the cell is automatically
   adjusted according to the table content which is centered in the cell.
3. The data of the table is stored in a two-dimensional list, so the program contains a lot of
   list operations, especially using list comprehension to create lists, which makes
   the program more concise.
"""

from random import randint


def get_width(text):
    """Get total width of text. Chinese characters count as two because the width ratio of Chinese
    to Western characters is 2:1.
    
    text: a string that may contain characters of different widths.
    """
    width = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # Unicode scope of Chinese characters.
            width += 2
        else:
            width += 1
    return width


class Table:
    """Table
    
    Atrributes
    ----------
    row_headers: list of row headers.
    col_headers: list of column headers.
    row_count: number of rows.
    col_count: number of columns.
    shape: shape of the table in string form of "m x n".
    data: two-dimensional list storing the data of table. Use data[row][column] to
          retrieve data in a cell. The index starts from 0.

    Methods
    -------
    fill(value=0): set all data to value.
    random(start=0, end=20): randomly set all data to integers between start and end.
    clear(row, col): clear data from all cells, a row, a column, or a cell.
    del_row(*rows): delete the specified rows of the table.
    del_col(*cols): delete the specified columns of the table.
    """
    def __init__(self, row_count=2, col_count=4, row_headers=None, col_headers=None):
        """Construct all the necessary attributes for the table object.

        row_count:
            number of rows.
        col_count:
            number of columns.
        row_headers: 
            list of row headers. If not given, the row headers will be "Row0, Row1...".
        col_headers:
            list of column headers. If not given, the column headers will be "Column0, Column1...".

        Table():
            instantiate a new table of 2 rows and 4 columns.
        Table(row_count, col_count):
            instantiate a new table of specified number of rows and columns.
        Table(row_headers, col_headers):
            instantiate a new table with specified row and column headers. The number of rows
            and columns of the table only depend on the number of elements in row_headers and
            col_headers. In this case, parameters row_count and col_count will be ignored.
        """
        if not row_headers:
            self.row_headers = ['Row' + str(i) for i in range(row_count)]
            self.row_count = row_count
        else:
            self.row_headers = row_headers
            self.row_count = len(row_headers)
        if not col_headers:
            self.col_headers = ['Column' + str(i) for i in range(col_count)]
            self.col_count = col_count
        else:
            self.col_headers = col_headers
            self.col_count = len(col_headers)
        self.shape = str(self.row_count) + ' x ' + str(self.col_count)
        # Initialze all data as empty.
        self.data = [['' for j in range(self.col_count)] for i in range(self.row_count)]
        # An internal variable used when generating a string representation of a table object.
        self._cell_width = 0

    def fill(self, value=0):
        """Set all data to value."""
        self.data = [[value for j in range(self.col_count)] for i in range(self.row_count)]

    def random(self, start=0, end=20):
        """Randomly set all data to integers between start and end."""
        self.data = [[randint(start, end) for j in range(self.col_count)]
                     for i in range(self.row_count)]

    def clear(self, row, col):
        """Clear data from all cells, a row, a column, or a cell.
        
        clear(): clear all data.
        clear(row=m): clear data at row m.
        clear(col=n): clear data at column n.
        clear(row=m, col=n): clear data[m][n].
        """
        if row is not None and col is None:
            for j in range(self.col_count):
                self.data[row][j] = ''
        elif col is not None and row is None:
            for i in range(self.row_count):
                self.data[i][col] = ''
        elif row is not None and col is not None:
            self.data[row][col] = ''
        else:
            self.fill('')

    def del_row(self, *rows):
        """Delete specified rows of the table."""
        # Start deleting from larger index, so as not to affect smaller ones.
        rows = sorted(rows, reverse=True)
        for row in rows:
            del self.data[row]
            del self.row_headers[row]
            self.row_count -= 1
        self.shape = str(self.row_count) + " x " + str(self.col_count)

    def del_col(self, *cols):
        """Delete specified columns of the table."""
        # Start deleting from larger index, so as not to affect smaller ones.
        cols = sorted(cols, reverse=True)
        for row_data in self.data:
            for col in cols:
                del row_data[col]
        for col in cols:
            del self.col_headers[col]
            self.col_count -= 1
        self.shape = str(self.row_count) + " x " + str(self.col_count)

    def __repr__(self):
        """Return a string representation of the table."""
        string = '\n'

        def print_divider():
            """Print divider between rows."""
            nonlocal string
            for _ in range(self.col_count + 1):
                string += ('|' + '-' * self._cell_width)
            string += '|\n'

        def print_cell(cell):
            """Print a cell's data in the center of its cell."""
            nonlocal string
            space = self._cell_width - get_width(cell)
            space_after = space // 2
            space_before = space_after + space % 2
            string += ('|' + ' ' * space_before + cell + ' ' * space_after)

        def print_col_headers():
            """Print column headers."""
            nonlocal string
            string += ('|' + ' ' * self._cell_width)
            for text in self.col_headers:
                print_cell(text)
            string += '|\n'

        # Put all headers and data in a flattened list.
        all_cells = self.col_headers + self.row_headers + [str(x) for row in self.data for x in row]
        # The width of the cell is determined by the max width of all headers and data.
        self._cell_width = max(get_width(cell) for cell in all_cells) + 2
        print_divider()
        print_col_headers()
        print_divider()
        for i, text in enumerate(self.row_headers):
            print_cell(text)
            for j in range(self.col_count):
                print_cell(str(self.data[i][j]))
            string += '|\n'
            print_divider()
        return string


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    # A table containing data about the number of students from three classes who like
    # certain vegetables.
    vegetables = ['Tomato', 'Carrot', 'Cucumber', 'Corn']
    classes = ['Class1', 'Class2', 'Class3']
    table = Table(row_headers=classes, col_headers=vegetables)
    table.random()
    print(table)
    print(table.shape)
    table.del_row(1)
    table.del_col(2)
    print(table)
    print(table.shape)
