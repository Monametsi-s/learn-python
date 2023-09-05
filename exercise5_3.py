# In tiss function I used exclusive or since it evaluates logical 
# opposites as True 
def logical_opposites(a, b, day):
    """print true for logical opposites no matter the arguments"""
    print((a > b) ^ (a <= b))
    print((a >= b) ^ (a < b))
    print((a >= 18) ^ (a < 18))
    print((day == 3) ^ (day != 3))
    print((a >= 18) ^ (a < 18))
    print((day != 3 ) ^ (day == 3))

logical_opposites(2,2,2)

  