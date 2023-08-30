from itertools import count, permutations, combinations, product

'''import sys

def absolute_value(x):
    if x < 0:
        return -x
    return x

    
def test(did_pass):
    """Print the result of a test"""
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file). """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite() # Here is the call to run the test
print(sys.copyright)

def get_name(me):
    pass

def who():
    linenum = sys._getframe(1).f_lineno

# Dicts from python
"""dict_1 = dict(America = 'New York', Netherlands = 'Amsterdam', Botswana = 'Gaborone')
print(dict_1)
dict_1['Zambia'] = 'Lilongwe'


print('New York' not in dict_1)

dict_2 = dict_1.copy()
print(dict_2)
print(dict_2.get('Namibia'))
print(dict_2.popitem())
print(dict_2)
print(dict_2.popitem())
print(dict_2)
#print(dict_2.pop('Namibia'))

keys = {'Thamaga', 'Ramotswa', 'Kanye'}
dict_3 = dict.fromkeys(keys)
print(dict_3)

vals = ['Bakgatla', 'Tshwene', 'Maila']
i = 0
for key in dict_3:
    dict_3[key] = vals[i]
    i = i + 1
print(dict_3.values())
for i in dict_3.values():
    print(i)
for i in dict_3.items():
    print(i)
#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
#inclusive
for i in range(1,21):
    print(i)

test_list = [i for i in range(1,1000001)]
#print(test_list)
#print(min(test_list))
#print(max(test_list))
#print(sum(test_list))

#Odd numbers between 1 and 20
list_1 = [i for i in range(1,21,2)]
print(list_1)

#Multiles of 3 in a list
list_2 = [i for i in range(3,31,3)]
print(list_2)

#Generator Expressions
G = (i for i in range(10))
#G = list(G)
for val in G:
    print(val, end=' ')
G = (n ** 2 for n in range(12))
for val in G:
    print(val, end=' ')
for i in count():
    print(i, end=' ')
    if i >= 10: break


def print_square_root(x):
    if x <= 0:
        print("Positive numbers only, please.")
        return
    result = x**0.5
    print("The square root of", x, "is", result)
num = input("enter the number for suare root: ")
if type(num) != 'int':
    raise ValueError("Enter a Valid Number")
num = int(num)
square_root = print_square_root(num)
"""try:
    num = int(input("enter the number for suare root: "))
    square_root = print_square_root(num)
except ValueError:
    print("Enter a valid value.")
"""
def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

fibonacci(-10)

try:
    x = 1 / int(input("Enter number to divide: "))
except ValueError as err:
    print("Error class is: ", type(err))
    print("Error message is:", err)
except ZeroDivisionError as err:
    print("Error class is: ", type(err))
    print("Error message is:", err)

string_1 = 'Mylist'

string_2 = []
for i in string_1:
    string_2.append(i)
print(string_2)
for val,i in enumerate(string_2):
    print(val, i)
if string_2[0] == 'M':
    print("Word starts with M")


# Zip used to map values of many lists.
# Used to iterate over multiple lists simultaneously
first_names = ['Mona', 'Juni', 'Titi']
second_names = ['Gee', 'joseph', 'reba']
numbers = [10, 20, 30]

for i, j, k in zip(first_names, second_names, numbers):
    print(i, j, k)

#Map iterator takes a function and applies it to the values in an iterator
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end=' ')
print()

#filter function prints values for which the filter function evaluates to True
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(30)):
    print(val, end=' ')
print()
'''
p = permutations(range(4),2)
print(*p)
c = combinations(range(4), 2)
print(*c)
list_1 = ['a', 'b']
list_2 = [1, 2, 3]
p1 = product(list_1, list_2)
print(*p1)

