from sorting.sortingfuncsplus import *

#Sorting Functions

def bubbleSort(arr, mode, rev):
    #Greater element bubbles up to the top
    n = len(arr)
    for _ in range(n): #Checks through all the elements
        for i in range(n-1): #Helping the singular element compare with the rest and bubble up
            if (mode == 1):
                if (rev == 1):
                    if (arr[i].get_name().upper() > arr[i+1].get_name().upper()): #if previous variable greater than next variable  swap the 2
                        arr[i], arr[i+1] = arr[i+1], arr[i] #no need of storing temp variable
                else:
                    if (arr[i].get_name().upper() < arr[i+1].get_name().upper()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]    
            elif (mode == 2):
                if (rev == 1):
                    if (arr[i].get_packname().upper() > arr[i+1].get_packname().upper()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if (arr[i].get_packname().upper() < arr[i+1].get_packname().upper()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
            elif (mode == 3):
                if (rev == 1):
                    if (arr[i].get_paxnum() > arr[i+1].get_paxnum()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if (arr[i].get_paxnum() < arr[i+1].get_paxnum()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]                   
            elif (mode == 4):
                if (rev == 1):
                    if (arr[i].get_packcost() > arr[i+1].get_packcost()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if (arr[i].get_packcost() < arr[i+1].get_packcost()):
                        arr[i], arr[i+1] = arr[i+1], arr[i]
    
def selectionSort(arr, mode, rev):
    n = len(arr)
    for i in range(n): #Checking for all elements
        lowest = i
        for j in range(i+1,n): #To compare through all the elements. If the lowest is greater than the element its compared with. The index of the element is stored in the lowest variable instead and the loop continues
            if (mode == 1):
                if (rev == 1):
                    if (arr[j].get_name().upper() < arr[lowest].get_name().upper()):
                        lowest = j
                else:
                    if (arr[j].get_name().upper() > arr[lowest].get_name().upper()):
                        lowest = j
            if (mode == 2):
                if (rev == 1):
                    if (arr[j].get_packname().upper() < arr[lowest].get_packname().upper()):
                        lowest = j
                else:
                    if (arr[j].get_packname().upper() > arr[lowest].get_packname().upper()):
                        lowest = j
            if (mode == 3):
                if (rev == 1):
                    if (arr[j].get_paxnum() < arr[lowest].get_paxnum()):
                        lowest = j
                else:
                    if (arr[j].get_paxnum() > arr[lowest].get_paxnum()):
                        lowest = j
            if (mode == 4):
                if (rev == 1):
                    if (arr[j].get_packcost() < arr[lowest].get_packcost()):
                        lowest = j
                else:
                    if (arr[j].get_packcost() > arr[lowest].get_packcost()):
                        lowest = j
    
        arr[i], arr[lowest] = arr[lowest], arr[i] #After comparison, the lowest varibale should have the index of the element with the lowest value, swap with the element that originally had the lowest title
    
def insertionSort(arr, mode, rev):
    #Similar to selection, where compares through all but it swaps instead of storing the index and swapping at the end
    n = len(arr)
    for i in range(1, n): #start from 1 due to checking with previous value and -1 will return the wrong number
        value = arr[i]
        current = i

        if (mode == 1):
            if (rev == 1):
                while (current > 0) and (arr[current-1].get_name().upper() > value.get_name().upper()):
                    arr[current] = arr[current-1] #Swaps the 2
                    current -= 1 #As the while loop goes on, it keeps checking if value is smaller and swaps with the backwards
            else:
                while (current > 0) and (arr[current-1].get_name().upper() < value.get_name().upper()):
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif (mode == 2):
            if (rev == 1):
                while (current > 0) and (arr[current-1].get_packname().upper() > value.get_packname().upper()):
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while (current > 0) and (arr[current-1].get_packname().upper() < value.get_packname().upper()):
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif (mode == 3):
            if (rev == 1):
                while (current > 0) and (arr[current-1].get_paxnum() > value.get_paxnum()):
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while (current > 0) and (arr[current-1].get_paxnum() < value.get_paxnum()):
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif (mode == 4):
            if (rev == 1):
                while (current > 0) and (arr[current-1].get_packcost() > value.get_packcost()):
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while (current > 0) and (arr[current-1].get_packcost() < value.get_packcost()):
                    arr[current] = arr[current-1] 
                    current -= 1 
        
        arr[current] = value #When the loop stops running, places the value at its correct index

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
