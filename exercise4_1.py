#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
#Write a function which is given the day number, and it returns the day name (a string).
from test_func import test
def day(day):
    """take a numnber and retun corresponding weekday."""
    match day:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case _:
            return "Days are from zero to six"

test(day(6) == "Saturday")
test(day(0) == "Sunday")
test(day(3) == "Wednesday")
test(day(8) == "Days are from zero to six")
test(day(-2) == "Days are from zero to six")


