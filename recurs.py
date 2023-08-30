import test_func
import sys
import os
import numpy

'''def r_sum(nested_num_list):
    """A recursive function to sum elements in a nested list"""
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

list = [1, 2, [3, 7,[1, 7, 9], 89, 10], 8, [2, 3], 5]
number = r_sum(list)
print(number)

def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        if first_time or val > largest:
            largest = val
        first_time = False
    return largest
assert r_max([2, 7, 8, [12, 6, [13, 47], 6]]) == 47
test_func.test(r_max([3, 8, 9, 12, 15, [4, 7, 8, [45, 89]],78 ]) == 89)

def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

recursion_depth(0)
'''


def get_dirlist(path):
    """
    lists the contents of a directory and all its subdirectories.
    Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names."""

    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "": 
        # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f) # Print the line
        fullname = os.path.join(path, f) # Turn name into full pathname
        if os.path.isdir(fullname): 
            # If a directory, recurse.
            print_files(fullname, prefix + "| ")


print_files('C:\\Users\\user\\Desktop\\Python_ Programming')
