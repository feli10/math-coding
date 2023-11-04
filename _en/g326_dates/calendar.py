"""Display calendar for a given month of a year."""

from datetime import date


CELL_WIDTH = 4
WEEKDAYS = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def display_calendar(year, month):
    """Display calendar for month of year.

    year:  integer between 1 and 9999
    month: integer between 1 and 12
    """
    # date.weekday() returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
    # first_weekday is the weekday of the first day of the month as an integer,
    # where Monday is 1 and Sunday is 7.
    first_weekday = date(year, month, 1).weekday() + 1
    if first_weekday == 7:
        first_weekday = 0

    day_count = DAYS_IN_MONTHS[month - 1]
    if month == 2 and is_leap_year(year):
        day_count += 1

    # Display calendar.
    # Print header.
    for weekday in WEEKDAYS:
        print(weekday.rjust(CELL_WIDTH), end='')
    print()
    # Print the beginning spaces of before the  first day.
    print(' ' * CELL_WIDTH * first_weekday, end='')
    # Print the days.
    for day in range(1, day_count + 1):
        print(str(day).rjust(CELL_WIDTH), end='')
        if (first_weekday + day) % 7 == 0:
            print()
    print()


year = int(input('Enter a year (1-9999): '))
month = int(input('Enter a month (1-12): '))
print()
display_calendar(year, month)
