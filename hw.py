from datetime import datetime


def add_date(date: str, days: int):
    # verify valid input
    if days < 0:
        raise (ValueError, "days to be added must contain a positive number")
    # convert date to datetime object
    cur_day, cur_month, cur_year = date_from_string(date)

    # calculate date
    while days > 0:
        cur_day, cur_month, cur_year, days = calculate_intermediate_date(cur_day, cur_month, cur_year, days)
    return date_to_string(cur_day, cur_month, cur_year)


def calculate_intermediate_date(date_day: int, date_month: int, date_year: int, days: int):
    # calc days of new date
    days_sum = date_day + days

    date_month_length = month_length(date_year, date_month)

    # assign new date values
    new_date_day = days_sum
    new_date_month = date_month
    new_date_year = date_year
    new_days = 0

    # check if sum is legal month length
    if days_sum > date_month_length:
        # update new date values
        new_date_day = 1
        new_date_month = date_month + 1 if date_month < 12 else 1
        new_date_year = date_year if date_month != 12 else date_year + 1
        new_days = days_sum - date_month_length - 1

    return new_date_day, new_date_month, new_date_year, new_days


def date_from_string(date: str, fmt: str = '%d.%m.%Y'):
    date = datetime.strptime(date, fmt)
    return date.day, date.month, date.year


def date_to_string(day: int, month: int, year: int, fmt: str = '%d.%m.%Y'):
    date = datetime(year=year, month=month, day=day)
    return date.strftime(fmt)


def month_length(year: int, month: int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    # leap year
    elif month == 2 and year % 4 == 0:
        return 29
    # not leap year
    elif month == 2 and year % 4 != 0:
        return 28
    else:
        raise (ValueError, "input value is not valid")


def main():
    inputs = [("10.01.2018", 10),
              ("29.06.2020", 8)]

    for i in range(len(inputs)):
        print(f"Input date: {inputs[i][0]}, Input days: {inputs[i][1]}, "
              f"output: {add_date(inputs[i][0], inputs[i][1])}")


if __name__ == "__main__":
    main()


