from sorting.sortingfuncsplus import *
from sorting.shortenfuncs import *

#Sorting Functions
"""
Bubble Sort Function

Greater Element Bubbles up to the top
First we check through all the elements using the for _ in range(n) loop
Then we check through all the elements using the for i in range(n-1) loop
For rev == 1: Meaning we sort in ascending order, if the element is greater than the next element swap the 2
For rev == 2: Descending order, we just swap the sign

Demonstration

Initial : [5,1,2]
First Loop : [1,5,2]
Second Loop : [1,2,5]
"""
def bubbleSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)

    for _ in range(n):
        for i in range(n-1):
            if (rev == 1):
                if (method(arr[i]) > method(arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if (method(arr[i]) < method(arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]

"""
Selection Sort Function

Compare element with all elements till lowest is found and swaps with the first index
First to ensure we check through all the elements, we use the for i in range(n) loop:
Then we check through the rest of the elements using the for j in range(i+1,n) loop
For rev == 1: Meaning we sort in ascending order, if the element is greater than the next element we assign the next index as lowest, we keep doing till we are through all the elements of the list. After that we swap the first element and the lowest element (based of lowest index)
For rev == 2: Descending order, we just swap the sign to make it so that the index of the highest value is stored in the lowest

Demonstration

Initial = [5,1,2]
First Loop : 
    lowest variable is assigned to index 1 or the value 5
    Since 1 is lesserr than 5, the index 2 is assigned to the lowest variable
Second Loop : 
    lowest variable stays assigned to index 2 as 1 is lesser than 2
After all comparisons with rest of the elements:
The element at index 1 (lowest variable) swaps with the first index:
[1,5,2]

This goes on for all elements
"""
def selectionSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)
    for i in range(n):
        lowest = i
        for j in range(i+1,n):
            if (rev == 1):
                if (method(arr[j]) < method(arr[lowest])):
                    lowest = j
            else:
                if (method(arr[j]) > method(arr[lowest])):
                    lowest = j
        
        arr[i], arr[lowest] = arr[lowest], arr[i]

"""
Insertion Sort Function

Similar to Selection, in terms of comparing through all elements in the list. However, Insertion works backwards and instead of storing the index, swaps the element with the previous element if the previous element is greater
The for i in range (1,n) starts from 1 due to us minusing the index by 1 if swap, hence if start from 0 will return index error / redundent code as the while loop will never be entered
The while loop basically checks the current element with the previous element, if the previous element is greater than the current element, we replace the current element with the previous element. The -= 1 is to continuously move down the list
arr[current] = value places the replaced value in the current index

Demonstration

Initial = [5,1,2]
First loop : 
    current = 1
    1 is greater than 5, so the current element gets replaced
    [5,5,2]
    The current value minuses one so = 0, exitting the loop
    Replacing the current with the replaced element
    [1,5,2]

Keeps going through all elements of the list
""" 
def insertionSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)
    for i in range(1,n):
        value = arr[i]
        current = i
        if (rev == 1):
            while (current > 0 and (method(arr[current-1]) > method(value))):
                arr[current] = arr[current-1]
                current -= 1
        else:
            while (current > 0 and (method(arr[current-1]) < method(value))):
                arr[current] = arr[current-1]
                current -= 1
        
        arr[current] = value

"""
Merge Sort Function

Merge Sort breaks the list into 2 halves, then recursively calls itself on the 2 halves until the list is 1 element
Then we merge the 2 halves together all the way till the list is sorted

Demonstration

Initial = [5,1,2,4]
First Split = [5,1] & [2,4]
Second Split = [5], [1], [2], [4]

Merge together = [1,5] , [2,4]
Merge Together = [1,2,4,5]

Keeps going through all elements of the list
""" 
def mergeSort(arr, mode, rev):
    if (len(arr) <= 1):
        return arr
    else:
        mid = len(arr) // 2

        lefthalf = mergeSort(arr[:mid], mode, rev)
        righthalf = mergeSort(arr[mid:], mode, rev)

        newList = mergeSortedList(lefthalf, righthalf, mode, rev)

        return newList

"""
Quick Sort Function

Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
Finds pivot where left side is smaller and right side is greater

Demonstration
***
""" 
def quickSort(array, low, high, mode, rev):
    if (low < high):
        pi = partition(array, low, high, mode, rev)

        quickSort(array, low, pi - 1, mode, rev)
        quickSort(array, pi + 1, high, mode, rev) 

"""
Counting Sort Function
better time complexity, though space complexity may be sacrificed when dealing with larger numbers

Counting Sort counts the number of occurences of each number
Length of count list will be the greatest number in the list

store cumulative count in the count list
Index = value. Then the number in that index will be where its placed in the new list
Minus one after using

Initialize count array
count = [0] * (greatest + 1)

for i in range(0, size) helps Store the count of each elements in count array

Stores the cummulative count
for i in range(1, len(count)):
    count[i] += count[i - 1]

Find the index of each element of the original array in count array
place the elements in output array
i = size - 1

demonstration

arr = [2,5,4,1]
count = [0,0,0,0,0]
after counting:
[0,1,1,0,1,1]

Cumulative:
[0,1,2,2,3,4]

For element 2, we look at index 2
The value is 2. The index of where 2 is placed is 2-1 = 1
[x,2,x,x]

For element 5, we look at index 5
the value is 4. the index of where 5 is placed is 4-1 =3
[x,2,x,5]

Done till sorted: 
[1,2,4,5]
"""
def countingSort(array, mode, rev):
    size = len(array)
    output = [0] * size
    newarr = []
    for i in range(len(array)):
        if (mode == 1):
            newarr.append(array[i].get_paxnum())
        else:
            newarr.append(array[i].get_packcost())
    greatest = max(newarr)

    count = [0] * (greatest + 1)

    for i in range(0, size):
        if (mode == 1):
            count[array[i].get_paxnum()] += 1
        else:
            count[array[i].get_packcost()] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = size - 1
    #Ascending
    if (rev == 1):
        while (i >= 0):
            if (mode == 1):
                output[count[array[i].get_paxnum()] - 1] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[count[array[i].get_packcost()] - 1] = array[i]
                count[array[i].get_packcost()] -= 1

            i -= 1

    else:
        #Descending
        while (i >= 0):
            if (mode == 1):
                output[-(count[array[i].get_paxnum()])] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[-(count[array[i].get_packcost()])] = array[i]
                count[array[i].get_packcost()] -= 1
            
            i -= 1

    return output

"""
Shell Sort (not as many comparisons as using intervals, better time complexity than the first 3, where compares with all)

Rearrange elements at each n/2, n/4, n/8, ... intervals
Compare using intervals , divide the intervals by 2 after completion of for loop with first interval

"""
def shellSort(array, mode, rev):
    method = determine_type(mode)
    n = len(array)
    interval = n // 2

    while (interval > 0):
        for i in range(interval, n):
            temp = array[i]
            j = i
            if (rev == 1):
                while (j >= interval) and (method(array[j-interval]) > method(temp)):
                    array[j] = array[j-interval]
                    j-= interval
            else:
                while (j >= interval) and (method(array[j-interval]) < method(temp)):
                    array[j] = array[j-interval]
                    j -= interval   
            
            array[j] = temp    

        interval //= 2

"""
Pancake Sort 

Using Findmax, find index of the greatest value

make the highest number the first index
the flips second argument being the maxind meaning the list flipped would be [element, element, element with maxind]

Then places the highest number at the end, by flipping the whole list

Size -= 1 : minus 1 to not touch the last element of the list

Demonstration

"""
def pancakeSort(arr, mode, rev):
    size = len(arr)
    while (size > 1):
        maxind = findMax(arr,size, mode , rev)
        
        if (maxind != size-1):
            flip(arr,maxind)

            flip(arr,size-1)

        size -= 1


"""
Comb Sort (Optimised Shell Sort Deals with gaps)

Creates the gap
while (gap > 1) or (swaps):
    gap = max(1, int(gap / 1.25))  # minimum gap is 1
    swaps = False
    for i in range(len(arr) - gap):
        j = i+gap

Demonstration

"""
def combsort(arr, mode, rev):
    method = determine_type(mode)
    gap = len(arr)
    swaps = True
    while (gap > 1) or (swaps):
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(arr) - gap):
            j = i+gap
            if (rev == 1):
                if (method(arr[i]) > method(arr[j])):
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps = True
            else:
                if (method(arr[i]) < method(arr[j])):
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps = True

"""
Cocktail Shaker Sort 



Demonstration

"""
def cocktail_shaker_sort(nums, mode, rev):
    method = determine_type(mode)
    for i in range(len(nums)-1, 0, -1):
        is_swapped = False
        if (rev == 1):
            for j in range(i, 0, -1):
                if (method(nums[j] < method(nums[j-1]))):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    is_swapped = True

            for j in range(i):
                if (method(nums[j] > method(nums[j+1]))):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_swapped = True
        else:
            for j in range(i, 0, -1):
                if (method(nums[j] > method(nums[j-1]))):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    is_swapped = True

            for j in range(i):
                if (method(nums[j] < method(nums[j+1]))):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_swapped = True

        if (not is_swapped):
            return nums

"""
Heap Sort 

Complete binary tree

Build max heap, its // 2 because any more would result in useless loops 

Swap last element with first element (should be greatest due to maxheap)
arr[i], arr[0] = arr[0], arr[i]

Heapify new root element then redo the whole process
heapify(arr, i, 0, mode, rev)

Demonstration

"""
def heapSort(arr, mode, rev):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i, mode, rev)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, mode, rev)
