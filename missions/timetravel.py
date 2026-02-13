import datetime

now = datetime.datetime.now()

print(now)

future = now + datetime.timedelta(days=100)
print("Date 100 days from now:", future)
