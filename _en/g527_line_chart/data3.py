"""Improve Data class to draw multi-line charts.

Some Useful Information:
1. The program adds the line() method for drawing multi-line charts to the Data class in 
   data2.py (G428). Except for the newly added method, the rest of the code in the 
   Data class remains unchanged.
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from g323_table.table import Table


class Data(Table):
    """Data class is a subclass of Table class. Data class inherits all attributes and methods of
    Table class. It also has methods to draw grouped bar charts and calculate average values.

    Methods
    -------
    bar(*row): draw a vertical grouped bar chart for given rows of the table.
    barh(*row): draw a horizontal grouped bar chart for given rows of the table.
    avg_row(row): calculate the average of the given row or of each row if row is not given.
    avg_col(col): calculate the average of the given column or of each column if col is not given.
    line(*row): draw a multi-line chart for given rows of the table.
    """
    def bar(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """Draw a vertical grouped bar chart for given rows of the table.

        rows: which rows of the table to draw, default is all rows.
        title: title of grouped bar chart.
        xlabel: x label for grouped bar chart.
        ylabel: y label for grouped bar chart.
        int_tick: whether ticks must be integers.
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # If no row is given, draw all rows.
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        # Set the width of a group of bars according to the number of bars contained in the group.
        if n == 1:
            WIDTH = 0.4
        elif n < 5:
            WIDTH = 0.6
        else:
            WIDTH = 0.8
        # Get the width of a single bar.
        width = WIDTH / n
        x = range(self.col_count)
        for i, row in enumerate(rows):
            # Get the position of the midpoint of each bar in a set of bars representing a row of
            # data on the grouped bar chart.
            pos = [value - WIDTH/2 + width/2 + width * i for value in x]
            rect = ax.bar(pos, self.data[row], width=width, label=self.row_headers[row])
            ax.bar_label(rect)
        ax.set_xticks(x, self.col_headers)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        plt.show()

    def barh(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """Draw a horizontal grouped bar chart for given rows of the table.

        rows: which rows of the table to draw, default is all rows.
        title: title of grouped bar chart.
        xlabel: x label for grouped bar chart.
        ylabel: y label for grouped bar chart.
        int_tick: whether ticks must be integers.
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # If no row is given, draw all rows.
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        # Set the height of a group of bars according to the number of bars contained in the group.
        if n == 1:
            HEIGHT = 0.4
        elif n < 5:
            HEIGHT = 0.6
        else:
            HEIGHT = 0.8
        # Get the height of a single bar.
        height = HEIGHT / n
        y = range(self.col_count)
        for i, row in enumerate(rows):
            # Get the position of the midpoint of each bar in a set of bars representing a row of
            # data on the grouped bar chart.
            pos = [value + HEIGHT/2 - height/2 - height * i for value in y]
            rect = ax.barh(pos, self.data[row], height=height, label=self.row_headers[row])
            ax.bar_label(rect)
        ax.set_yticks(y, self.col_headers)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        plt.show()

    def avg_row(self, row=None, rounding=0):
        """Calculate the average of the given row. If row is not given, a list of each row's
        average value will be returned.

        row: row for which its average will be calculated. If not given, calculate the average
             of each row.
        rounding: the number of decimal places the result should be rounded to.
        """
        def avg_one_row(row):
            """Calculate the average of the given row."""
            avg = sum(self.data[row])/self.col_count
            if rounding == 0:
                return round(avg)
            return round(avg, rounding)

        if row is not None:
            return avg_one_row(row)
        avgs = []
        for i in range(self.row_count):
            avgs.append(avg_one_row(i))
        return avgs

    def avg_col(self, col=None, rounding=0):
        """Calculate the average of the given column. If column is not given, a list of each
        column's average value will be returned.

        col: column for which its average will be calculated. If not given, calculate the average
             of each column.
        rounding: the number of decimal places the result should be rounded to.
        """
        def avg_one_col(col):
            """Calculate the average of the given column."""
            total = 0
            for i in range(self.row_count):
                total += self.data[i][col]
            avg = total / self.row_count
            if rounding == 0:
                return round(avg)
            return round(avg, rounding)

        if col is not None:
            return avg_one_col(col)
        avgs = []
        for j in range(self.col_count):
            avgs.append(avg_one_col(j))
        return avgs

    def line(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """Draw a multi-line chart for given rows of the table.

        rows: which rows of the table to draw, default is all rows.
        title: title of multi-line chart.
        xlabel: x label for multi-line chart.
        ylabel: y label for multi-line chart.
        int_tick: whether ticks must be integers.
        """
        _, ax = plt.subplots()
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # If no row is given, draw all rows.
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        n = len(rows)
        # Draw the multi-line chart.
        for row in rows:
            ax.plot(self.col_headers, self.data[row], marker='o', label=self.row_headers[row])
            # Annotate the values on top of each point.
            for i in range(self.col_count):
                ax.annotate(str(self.data[row][i]), (i, self.data[row][i]),
                            textcoords='offset points', xytext=(0, 6), ha='center')
        ax.set_yticks(list(range(MAX_HOURS * 2)))
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        ax.grid(True)
        plt.show()


MAX_HOURS = 3
TITLE = 'Daily Study Time'
XLABEL = 'Day'
YLABEL = 'Hours Spent'
DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
SUBJECTS = ['Math', 'Music', 'P.E.']

# Create data object and generate data for it.
data = Data(row_headers=SUBJECTS, col_headers=DAYS)
data.random(0, 3)
print(data)

# Draw multi-line charts.
data.line(title=TITLE, xlabel=XLABEL, ylabel=YLABEL)
