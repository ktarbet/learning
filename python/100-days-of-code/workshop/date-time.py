import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(type(now.second))
print(now.second)
print(now.weekday())

today = dt.datetime(year=2024, month=2, day=21)
print(today)

if now.weekday() == today.weekday():
    print("hi")
    pass
