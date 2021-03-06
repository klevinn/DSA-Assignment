import random
from time import sleep
from threading import Timer
from sorting.slowsortingfuncsplus import *
from general.shortenfuncs import *

"""
Bad Sorts : Bogo Sort
    Best Time Complexity: O(n)
    Worst Time Complexity: O(inf) as this algorithm has no upper bound
    Average Time Complexity: O(n*n!)

Randomly Shuffles the list untill it gets sorted. High chance of never sorting
"""
def bogoSort(arr, mode, rev):
    i = 1
    while (is_sorted(arr, mode, rev) == False):
        shuffle(arr)
        print("Sort %d : Unsuccessful" %(i), end="\r")
        i += 1
    
    print("Sort %d : Successful" %(i))

"""
Bad Sorts : Stalin Sort
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n)
    Average Time Complexity: O(n)

VERY EFFICIENT!!!

Removes Elements that are unsorted.
"""
def stalinSort(arr, mode, rev):
    method = determine_type(mode)
    if (len(arr) < 1):
        return arr
    val = arr[0]
    newarr = []
    for i in arr:
        if (rev == 1):
            if (method(i) >= method(val)):
                newarr.append(i)
                val = i
        else:
            if (method(i) <= method(val)):
                newarr.append(i)
                val = i

    return newarr

"""
Bad Sorts : Slow Sort
    Best Time Complexity: O(n^2.709)
    Worst Time Complexity: O(n^2.709)
    Average Time Complexity: O(n^2.709)

Greater than O(n^2)

Multiply & Surrender Algorithm
"""
def slow_sort(A, i, j, mode, rev):
    method = determine_type(mode)
    #Recursion Break
    if (i >= j):
        return

    #Store Middle Values
    m = (i+j) // 2

    #Reecursively call left half and right halg

    slow_sort(A, i, m, mode, rev)
    slow_sort(A, m + 1, j, mode, rev)

    if (rev == 1):
    #Swap first and second ele if First < than secon
        if (method(A[j]) < method(A[m])):
            A[m], A[j] = A[j], A[m]
    else:
        if (method(A[j]) > method(A[m])):
            A[m], A[j] = A[j], A[m]
    
    slow_sort(A, i, j-1, mode, rev)

"""
Bad Sorts : Sleep Sort
    Best Time Complexity: O(max(arr))
    Worst Time Complexity: O(max(arr))
    Average Time Complexity: O(max(arr))

Code sleeps based of the number and is appended after that amount of time
"""
def sleep_sort(arr, mode, rev):
    result = []
    def add1(x):
        result.append(x)

    ind = arr[0]
    for i in arr:
        if (mode == 1):
            if (ind.get_paxnum() < i.get_paxnum()): ind = i
            Timer(i.get_paxnum(), add1, [i]).start()
        else:
            if (ind.get_packcost() < i.get_packcost()): ind = i
            Timer(i.get_packcost(), add1, [i]).start()

    if (mode == 1):
        sleep(ind.get_paxnum()+1)
    elif (mode == 2):
        sleep(ind.get_packcost()+1)
    
    if (rev == 1):
        return result
    else:
        return result[::-1]

"""
Bad Sorts : Gnome Sort
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n^2)
    Average Time Complexity: O(n^2)

Gnome sort is a sorting algorithm that works by  comparing the current element with the previous element
They swap if not correctly ordered

"""
def gnomeSort(arr, mode , rev):
    method = determine_type(mode)
    n = len(arr)
    index = 0
    while (index < n):
        if (index == 0):
            index += 1

        if (rev == 1):
            if (method(arr[index]) >= method(arr[index-1])):
                index += 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index -= 1
        else:
            if (method(arr[index]) <= method(arr[index-1])):
                index += 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index -= 1
