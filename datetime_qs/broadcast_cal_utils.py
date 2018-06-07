"""util functions for broadcast calendar

   https://en.wikipedia.org/wiki/Broadcast_calendar
"""

import datetime


def broadcast_month_start(year, month):
    """return start of broadcast month. always on monday"""
    start_date = datetime.datetime(year, month, 1)
    while start_date.weekday() != 0:
        start_date -= datetime.timedelta(days=1)
    return start_date

def quarter_start_month(quarter):
    """month that starts quarter for Gregorian calendar: Jan, Apr, Jul, Oct"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    return 3 * quarter - 2

def get_quarter(month):
    """return quarter for month"""
    if month not in range(1, 13):
        raise ValueError("invalid month")
    return (month + 2) // 3

def next_quarter(year, quarter):
    """return next quarter for Gregorian calendar"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    if quarter == 4:
        return year+1, 1
    else:
        return year, quarter+1

def broadcast_quarter_dates(year, quarter, num=1):
    """start and end dates for broadcast quarter"""
    month = quarter_start_month(quarter)
    start = broadcast_month_start(year, month)

    # calculate end of quarter based on start of subsequent quarter
    for _ in range(num):
        year, quarter = next_quarter(year, quarter)
    month = quarter_start_month(quarter) #maybe next_quarter returns month?
    end = broadcast_month_start(year, month) - datetime.timedelta(days=1)

    return start, end

def next_quarter_broadcast_dates(num=1, start_offset=0, end_offset=0):
    """return dates for next broadcast quarter (from now)"""
    now = datetime.datetime.today()
    year = now.year
    quarter = get_quarter(now.month)

    while True:
        start, end = broadcast_quarter_dates(year, quarter, num)
        if now < start:
            break
        year, quarter = next_quarter(year, quarter)

    return (start+datetime.timedelta(days=start_offset),
            end+datetime.timedelta(days=end_offset))

def next_monday():
    """return datetime for next monday"""
    temp = datetime.datetime.today()
    # *next* monday, don't return today if it's monday
    while True:
        temp += datetime.timedelta(days=1)
        if temp.weekday() == 0:
            return temp
