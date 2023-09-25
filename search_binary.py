from test_func import test
import math
import cmath
def search_binary(list, target):
    low = 0
    high = len(list)

    
    while True:
        if low == high:
            return -1
                
        mid_index = (low + high) // 2
        if list[mid_index] == target:
            return mid_index
        if list[mid_index] > target:
            high = mid_index
        elif list[mid_index] < target:
            low = mid_index + 1





  
list = [1, 2, 5, 8, 15, 17, 19, 25] 
search_binary(list, 5)


test(search_binary(list, 25) == 7)
test(search_binary(list, 2) == 1)
test(search_binary(list, 5) == 2)
test(search_binary(list, 15) == 4)

'''test(search_binary(list, 17) == 6)
test(search_binary(list, 54) == -1)
test(search_binary(list, 60) == 5) 
test(search_binary(list, 33) == 2)
test(search_binary(list, 8) == 7)
test(search_binary(list, 5) == 3)
test(search_binary(list, 15) == 4)'''