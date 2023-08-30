import time
#from test_func import test 
list = [i for i in range(10000000)]
list_1 = [1, 4, 5, 6, 7, 8]
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"] 
def linear(list, num):
    """find and return the index of an item in a sequence"""
    for i,j in enumerate(list):
        if list[i] == num:
            return i

    return -1

t0 = time.process_time_ns()
index = linear(list, 805600)
t1 = time.process_time_ns()

print("time taken for linear search is {0:.5f}".format(t1-t0))
#t.test((linear(friends, "Angelina") == 3))
#t.test((linear(friends, "Zuki") == 4))
#t.test((linear(friends, "May") == -1))

