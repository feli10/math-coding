"""Use Matplotlib to draw bar charts in two coding styles.

Some Useful Information:
1. In Matplotlib, a Figure is the whole figure in a window and may includes one or more Axes
   (or Subplots). The Figure keeps track of all the child Axes and other components.
2. There are essentially two ways to use Matplotlib:
   (https://matplotlib.org/stable/users/explain/quick_start.html#coding-styles)
   - Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO)
     style").
   - Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot
     functions for plotting.
   In general, Matplotlib suggests using the OO-style, particularly for complicated plots. However,
   the pyplot-style can be very convenient for quick interactive work.
3. For comparison, this program uses Matplotlib to draw bar charts in two figures, using one of two
   coding styles for each figure. The two figures are exactly the same.
4. Each figure includes two axes in one row and two columns. The first axes is a vertical bar
   chart, and the second is a horizontal bar chart.
"""

from random import randint
import matplotlib.pyplot as plt


RAND_MAX = 50
TITLE = 'Number of Students Who Like Certain Vegetables'
LABEL_ITEM = 'Vegetables'
LABEL_VALUE = 'No. of Likes'
ITEMS = ['Tomato', 'Carrot', 'Cucumber', 'Corn', 'Pepper']


def explicit_oo_style():
    """Draw a vertical bar chart and a horizontal bar chart in a figure using Matplotlib's
    explicit OO-style.
    """
    # Create a new figure with two axes in one row and two columns.
    fig, axs = plt.subplots(1, 2, figsize=(18, 6))
    fig.suptitle(TITLE)
    # Draw a vertical bar chart in the first axes.
    axs[0].bar(ITEMS, values, width=0.4)
    axs[0].set_title('Vertical Bar Chart')
    axs[0].set_xlabel(LABEL_ITEM)
    axs[0].set_ylabel(LABEL_VALUE)
    # Draw a horizontal bar chart in the second axes.
    axs[1].barh(ITEMS, values, color='maroon', height=0.4)
    axs[1].set_title('Horizontal Bar Chart')
    axs[1].set_xlabel(LABEL_VALUE)
    axs[1].set_ylabel(LABEL_ITEM)


def implicit_pyplot_style():
    """Draw a vertical bar chart and a horizontal bar chart in a figure using Matplotlib's
    implicit pyplot-style.
    """
    # Create a new figure.
    plt.figure(figsize=(18, 6))
    plt.suptitle(TITLE)
    # Add an axes to the figure at the first row and the first column and use it as current axes.
    plt.subplot(121)
    # Draw a vertical bar chart in current axes.
    plt.bar(ITEMS, values, width=0.4)
    plt.title('Vertical Bar Chart')
    plt.xlabel(LABEL_ITEM)
    plt.ylabel(LABEL_VALUE)
    # Add an axes to the figure at the first row and the second column and use it as current axes.
    plt.subplot(122)
    # Draw a horizontal bar chart in current axes.
    plt.barh(ITEMS, values, color='maroon', height=0.4)
    plt.title('Horizontal Bar Chart')
    plt.xlabel(LABEL_VALUE)
    plt.ylabel(LABEL_ITEM)


# Generate random data.
values = []
for i in range(len(ITEMS)):
    values.append(randint(0, RAND_MAX))

# Use Matplotlib to draw bar charts in two coding styles. The two figures are exactly the same.
explicit_oo_style()
implicit_pyplot_style()

# Display all open figures.
plt.show()
