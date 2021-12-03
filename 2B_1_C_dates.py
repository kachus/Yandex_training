date, month, year=input().split()
date=int(date)
month=int(month)
year=int(year)
if (date>12 or month>12) or month==date:
    print(1)
else:
    print(0)