from exercise4_1 import day
from test_func import test

def return_day(leave_day, days_after):
            if isinstance(leave_day, str) or isinstance(days_after, str):
                if isinstance(leave_day, str):
                    return "leave day should be a number"
                if isinstance(days_after, str):
                    return "return day should be a number"    
            elif isinstance(leave_day, int) and isinstance(days_after, int):
                if leave_day not in range(7):
                    return "Day is not within range"
                total_days = leave_day+days_after
                if total_days < 7:
                    return day(total_days)
                else:
                    rem_days = total_days % 7
                    return day(rem_days)
            else:
                return "Enter a valid day"

test(return_day(3,2) == "Friday")
test(return_day(4,2) == "Saturday")
test(return_day("Monday", 54) == "leave day should be a number")
test(return_day(5, "Sunday") == "return day should be a number")

