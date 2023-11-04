"""Create Data class (a subclass of Table class) and add two mehtods to Data class to draw
vertical and horizontal bar charts.
"""

import sys
import matplotlib.pyplot as plt
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from g323_table.table import Table


class Data(Table):
    """Data class is a subclass of Table class. Data class inherits all attributes and methods of
    Table class. It also has two additional methods for drawing bar charts.

    Methods
    -------
    bar(row=0): draw a vertical bar chart for a given row of the table (row 0 by default).
    barh(row=0): draw a horizontal bar chart for a given row of the table (row 0 by default).
    """
    def bar(self, row=0, title=None, xlabel=None, ylabel=None, int_tick=True):
        """Draw a vertical bar chart for a given row of the table.

        row: which row of the table to draw, default is row 0.
        title: title of bar chart.
        xlabel: x label for bar chart.
        ylabel: y label for bar chart, default is the row's header.
        int_tick: whether ticks must be integers.
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        ax.bar(self.col_headers, self.data[row], width=0.4)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel if ylabel is not None else self.row_headers[row])
        plt.show()

    def barh(self, row=0, title=None, xlabel=None, ylabel=None, int_tick=True):
        """Draw a horizontal bar chart for a given row of the table.

        row: which row of the table to draw, default is row 0.
        title: title of bar chart.
        xlabel: x label for bar chart, default is the row's header.
        ylabel: y label for bar chart.
        int_tick: whether ticks must be integers.
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        ax.barh(self.col_headers, self.data[row], height=0.4)
        ax.set_title(title)
        ax.set_xlabel(xlabel if xlabel is not None else self.row_headers[row])
        ax.set_ylabel(ylabel)
        plt.show()


TITLE = 'Number of Students Who Like Certain Vegetables'
LABEL_ITEM = 'Vegetables'
LABEL_VALUE = ['No. of Likes']
VEGETABLES = ['Tomato', 'Carrot', 'Cucumber', 'Corn']

data = Data(row_headers=LABEL_VALUE, col_headers=VEGETABLES)
data.random()
print(data)
data.bar(title=TITLE, xlabel=LABEL_ITEM)
data.barh(title=TITLE, ylabel=LABEL_ITEM)
