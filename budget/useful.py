import datetime

def get_timeframe(f,l):
    timeframe = []
    f_months = range(f.date.month, 13)
    l_months = range(1, l.date.month+1)
    if f.date.year == l.date.year:
        for m in range(f.date.month, l.date.month+1):
            timeframe.append([m, f.date.year])
        return timeframe
    for m in f_months:
        timeframe.append([m, f.date.year])

    for y in range(f.date.year+1, l.date.year):
        for m in range(f.date.month+1, l.date.month):
            timeframe.append([m, y])

    for m in l_months:
        timeframe.append([m, l.date.year])
    return timeframe

