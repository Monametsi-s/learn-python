from exercise4_1 import day
from test_func import test

def return_day(leave_day, days_after):
    if leave_day not in range(7):
        return "Day is not within range"
    
    total_days = leave_day+days_after
    if total_days < 7:
        return day(total_days)
    else:
        rem_days = total_days % 7
        return day(rem_days)


test(return_day(3,2) == "Friday")
test(return_day(4,2) == "Saturday")