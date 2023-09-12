from test_func import test
   
def linear(list, num):
    for i, j in enumerate(list):
        if j == num:
            return i
    return -1

list = [1, 2, 33, 24, 15, 60, 17, 8] 

test(linear(list, 17) == 6)
test(linear(list, 54) == -1)
test(linear(list, 60) == 5) 
test(linear(list, 1) == 0)