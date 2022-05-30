from sorting.shortenfuncs import *

#File for extra functions needed in Sort Functions

"""
#MergeSort : Combining the Split Sorted Lists

First initiate a whileloop that will end once an out of range error will occur (one of the saved variables of the index exceed te length)

As he loop goes through they will compare the values of thee element of each list
If the value is lesser than, the element will be appended first, and the index they are checking will add 1
Then this process will go through untill the while condition is reached.

Since its possible for there to be leftover elements in the list. After the while loop we add anything remaining into the result from the index that breaks the while loop

First pass (Looking at both index 0): 
Left - [1,5,6,7,9]
Right - [2,3,4,8]

IDE sees 1 is lesser than 2:
FinalArr - [1]

Second Pass (Looking at left index 1 and right index 0):
IDE sees 2 is lesser than 5
FinalArr - [1,2]

Third Pass (Looks at left index 1 and right index 1):
...
"""
def mergeSortedList(left, right, mode, rev):
    method = determine_type(mode)
    leftInd = 0
    rightInd = 0
    result = []
    
    if (rev == 1):
        while (leftInd < len(left) and (rightInd < len(right))):
            if (method(left[leftInd]) < method(right[rightInd])):
                result.append(left[leftInd])
                leftInd += 1
            else:
                result.append(right[rightInd])
                rightInd += 1
    else:
        while (leftInd < len(left) and (rightInd < len(right))):
            if (method(left[leftInd]) > method(right[rightInd])):
                result.append(left[leftInd])
                leftInd += 1
            else:
                result.append(right[rightInd])
                rightInd += 1   

    result += left[leftInd:]
    result += right[rightInd:]
    return result

"""
QuickSort : Partitioning the List

Pivot is the last element
Pointer for the greater element
The for j in range(low,high), compares all the list elements bteeen the pivot
If element is greater than the pivot, it will be swapped with the greater element
"""
def partition(array, low, high, mode, rev):
    method = determine_type(mode)
    pivot = array[high]
    i = low - 1 
    for j in range(low,high):
        if (rev == 1):
            if method(array[j]) <= method(pivot):
                i += 1
                array[i], array[j] = array[j], array[i]
        else:
            if method(array[j]) >= method(pivot):
                i += 1
                array[i], array[j] = array[j], array[i]
    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1

"""
Heap Sort : Creating the Max heap

Order of elements is the level order traversal of the tree
Build max heap by swapping the root with the node (higher node on top)

Find largest among root and children
Greatest index placed into the heapify(), the i variable = The root node

Since its a complete binary tree, where the order of elements in an array is the level order traversal of the tree. the left and right subtree of the root is always decided by a set formula
l = 2 * i + 1 #Left node of the root (i) 
r = 2 * i + 2 #right node of the root (i)

if l < n : checking if the element suppsoed to be in the left tree exists, if more than len means doesnt exist
if r < n : checkign right element if exists, and checking if right element is greater than the left element if exists
checking if the subtree node is greater, if greater the element number takes the largest

If largest != i: If root is not largest, swap with largest and continue heapifying, to ensure that the nodes new position, is still the max heap
"""
def heapify(arr, n, i, mode, rev):
    method = determine_type(mode)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 

    if (rev == 1):
        if (l < n) and (method(arr[i]) < method(arr[l])):
            largest = l
        if (r < n) and (method(arr[largest]) < method(arr[r])):
            largest = r
    else:
        if (l < n) and (method(arr[i]) > method(arr[l])):
            largest = l
        if (r < n) and (method(arr[largest]) > method(arr[r])):
            largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest,mode, rev)

"""
Pancake Sort Functions : Flip, FindMax
Flip just reverses the array.

FindMax returns the index of the greatest number in the array
"""
def flip(arr, i):
    start = 0
    while (start < i):
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def findMax(arr, n, mode, rev):
    method = determine_type(mode)
    maxindex = 0
    for i in range(0,n):
        if (rev == 1):
            if (method(arr[i]) > method(arr[maxindex])):
                maxindex = i
        else:
            if (method(arr[i]) < method(arr[maxindex])):
                maxindex = i

    return maxindex
