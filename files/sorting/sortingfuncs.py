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

def mergeSort(arr, mode, rev):
    if (len(arr) <= 1):
        return arr
    else:
        mid = len(arr) // 2

        lefthalf = mergeSort(arr[:mid], mode, rev)
        righthalf = mergeSort(arr[mid:], mode, rev)

        newList = mergeSortedList(lefthalf, righthalf, mode, rev)

        return newList

def quickSort(array, low, high, mode, rev):
    if (low < high):
        pi = partition(array, low, high, mode, rev) #find pivot where left side is smaller and ride side is greater

        #sorting left side and right side again respectively
        quickSort(array, low, pi - 1, mode, rev) #left side
        quickSort(array, pi + 1, high, mode, rev) #right side

#better time complexity, though space complexity may be sacrificed when dealing with larger numbers
def countingSort(array, mode, rev):

    #Counting Sort counts the number of occurences of each number
    #Length of count list will be the greatest number in the list

    #store cumulative count in the count list
    #Index = value. Then the number in that index will be where its placed in the new list
    #Minus one after using

    size = len(array)
    output = [0] * size
    newarr = []
    for i in range(len(array)):
        if (mode == 1):
            newarr.append(array[i].get_paxnum())
        else:
            newarr.append(array[i].get_packcost())
    greatest = max(newarr)

    # Initialize count array
    count = [0] * (greatest + 1)

    # Store the count of each elements in count array
    for i in range(0, size):
        if (mode == 1):
            count[array[i].get_paxnum()] += 1
        else:
            count[array[i].get_packcost()] += 1
    

    # Store the cummulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]


    # Find the index of each element of the original array in count array
    # place the elements in output array
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

#not as many comparisons as using intervals, better time complexity than the first 3, where compares with all
def shellSort(array, mode, rev):

    n = len(array)

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    #Compare using intervals , divide the intervals by 2 after completion of for loop with first interval
    interval = n // 2
    while (interval > 0):
        for i in range(interval, n):          
            temp = array[i]
            j = i
            if (rev == 1):
                if (mode == 1):
                    while (j >= interval) and (array[j - interval].get_name().upper() > temp.get_name().upper()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 2):
                    while (j >= interval) and (array[j - interval].get_packname().upper() > temp.get_packname().upper()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 3):
                    while (j >= interval) and (array[j - interval].get_paxnum() > temp.get_paxnum()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 4):
                    while (j >= interval) and (array[j - interval].get_packcost() > temp.get_packcost()):
                        array[j] = array[j - interval]
                        j -= interval
            
            else:
                if (mode == 1):
                    while (j >= interval) and (array[j - interval].get_name().upper() < temp.get_name().upper()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 2):
                    while (j >= interval) and (array[j - interval].get_packname().upper() < temp.get_packname().upper()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 3):
                    while (j >= interval) and (array[j - interval].get_paxnum() < temp.get_paxnum()):
                        array[j] = array[j - interval]
                        j -= interval

                elif (mode == 4):
                    while (j >= interval) and (array[j - interval].get_packcost() < temp.get_packcost()):
                        array[j] = array[j - interval]
                        j -= interval

            array[j] = temp

        interval //= 2

def pancakeSort(arr, mode, rev):
    size = len(arr)
    while (size > 1):
        #find index of the greatest value
        maxind = findMax(arr,size, mode , rev)
        
        if (maxind != size-1):
            #make the highest number the first index
            #the flips second argument being the maxind meaning the list flipped would be [element, element, element with maxind]
            flip(arr,maxind)

            #Then places the highest number at the end, by flipping the whole list
            flip(arr,size-1)
        
        #minus 1 to not touch the last element of the list
        size -= 1

def combsort(arr, mode, rev):
    #optimised Shell sort?

    gap = len(arr)
    swaps = True
    while (gap > 1) or (swaps):
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(arr) - gap):
            j = i+gap

            if (rev == 1):
                if (mode == 1):
                    if (arr[i].get_name().upper() > arr[j].get_name().upper()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 2):
                    if (arr[i].get_packname().upper() > arr[j].get_packname().upper()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 3):
                    if (arr[i].get_paxnum() > arr[j].get_paxnum()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 4):
                    if (arr[i].get_packcost() > arr[j].get_packcost()):
                        arr[i], arr[j] = arr[j], arr[i]   
                        swaps = True
            else:
                if (mode == 1):
                    if (arr[i].get_name().upper() < arr[j].get_name().upper()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 2):
                    if (arr[i].get_packname().upper() < arr[j].get_packname().upper()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 3):
                    if (arr[i].get_paxnum() < arr[j].get_paxnum()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif (mode == 4):
                    if (arr[i].get_packcost() < arr[j].get_packcost()):
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True

def cocktail_shaker_sort(nums, mode, rev):
    for i in range(len(nums)-1, 0, -1):
        is_swapped = False
        
        if (rev == 1):
            if (mode == 1):
                for j in range(i, 0, -1): #Moving from right to left
                    if (nums[j].get_name().upper() < nums[j-1].get_name().upper()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i): #moving from left to right
                    if (nums[j].get_name().upper() > nums[j+1].get_name().upper()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 2):
                for j in range(i, 0, -1):
                    if (nums[j].get_packname().upper() < nums[j-1].get_packname().upper()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_packname().upper() > nums[j+1].get_packname().upper()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 3):
                for j in range(i, 0, -1):
                    if (nums[j].get_paxnum() < nums[j-1].get_paxnum()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_paxnum() > nums[j+1].get_paxnum()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 4):
                for j in range(i, 0, -1):
                    if (nums[j].get_packcost() < nums[j-1].get_packcost()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_packcost() > nums[j+1].get_packcost()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True
        
        else:
            if (mode == 1):
                for j in range(i, 0, -1):
                    if (nums[j].get_name().upper() > nums[j-1].get_name().upper()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_name().upper() < nums[j+1].get_name().upper()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 2):
                for j in range(i, 0, -1):
                    if (nums[j].get_packname().upper() > nums[j-1].get_packname().upper()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_packname().upper() < nums[j+1].get_packname().upper()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 3):
                for j in range(i, 0, -1):
                    if (nums[j].get_paxnum() > nums[j-1].get_paxnum()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_paxnum() < nums[j+1].get_paxnum()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif (mode == 4):
                for j in range(i, 0, -1):
                    if (nums[j].get_packcost() > nums[j-1].get_packcost()):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if (nums[j].get_packcost() < nums[j+1].get_packcost()):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True
        
        if (not is_swapped):
            return nums

def heapSort(arr, mode, rev):
    #complete binary tree
    n = len(arr)

    # Build max heap, its // 2 because any more would result in useless loops 
    for i in range(n//2, -1, -1):
        heapify(arr, n, i, mode, rev)

    for i in range(n-1, 0, -1):
        # Swap last element with first element (should be greatest due to maxheap)
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify new root element then redo the whole process
        heapify(arr, i, 0, mode, rev)
