import calendar
def day(year,month,date):
    day=calendar.weekday(int(year), int(month), int(date))
    print(calendar.day_name[day].upper())

day(2026,5,7)