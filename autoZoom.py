import calendar
import datetime
from days_n_links import *

#get current time
now = datetime.datetime.now()


# seperated
d = now.strftime("%d")
m = now.strftime("%m")
y = now.strftime("%y")

# formatted vars
year = "20" + str(y)
yearForm = int(year)
month = int(m)
day = int(d)

weekday = calendar.weekday(yearForm, month, day)

# monday = 0
# tuessay = 1
# wednessday = 2 
# thursday = 3
# friday = 4
# saturday = 5
# sunday = 6

print(weekday)

# decides what day it is for that Schedule
if weekday == 5 and 6:
    exit()
elif weekday == 0:
    monday()
elif weekday == 1:
    tuesday()
elif weekday == 2:
    wednessday()
elif weekday == 3:
    thursday()
elif weekday == 4:
    friday()
