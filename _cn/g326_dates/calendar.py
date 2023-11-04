"""显示某年某月的日历"""

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
    """显示给定年、月的日历。

    year:  表示年的整数, 1-9999。
    month: 表示月的整数, 1-12。
    """
    # date.weekday() 返回一个表示星期几的整数, 星期一是 0，星期日是 6。
    # first_weekday 某月一号是星期几，星期一是 1，星期日是 7。
    first_weekday = date(year, month, 1).weekday() + 1
    if first_weekday == 7:
        first_weekday = 0

    day_count = DAYS_IN_MONTHS[month - 1]
    if month == 2 and is_leap_year(year):
        day_count += 1

    # 显示日历。
    # 打印标题（星期日至星期六）。
    for weekday in WEEKDAYS:
        print(weekday.rjust(CELL_WIDTH), end='')
    print()
    # 打印该月第一日前面的空格。
    print(' ' * CELL_WIDTH * first_weekday, end='')
    # 打印该月每一日。
    for day in range(1, day_count + 1):
        print(str(day).rjust(CELL_WIDTH), end='')
        if (first_weekday + day) % 7 == 0:
            print()
    print()


year = int(input('输入年份 (1 - 9999): '))
month = int(input('输入月份 (1 - 12): '))
print()
display_calendar(year, month)
