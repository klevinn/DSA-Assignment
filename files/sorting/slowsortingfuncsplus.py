import random
from general.shortenfuncs import *

"""
Functions used by Slow Sorting Functions
"""

#To check if array is sorted or Not
def is_sorted(a, mode, rev):
    method = determine_type(mode)
    n = len(a)
    for i in range(0, n-1):
        if (rev == 1):
            if (method(a[i]) > method(a[i+1])):
                return False
        else:
            if (method(a[i]) < method(a[i+1])):
                return False

    return True

#To generate permutation of an array
def shuffle(arr):
    n = len(arr)
    for i in range(0,n):
        r = random.randint(0,n-1) #GEnerates a random number and swaps with the i
        arr[i], arr[r] = arr[r], arr[i]
