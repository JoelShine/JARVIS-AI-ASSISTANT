import calendar
import datetime

now = datetime.datetime.now()

print(calendar.month(int(now.strftime("%Y")), int(now.strftime("%m"))))
#print(calendar.calendar(int(now.strftime("%Y"))))