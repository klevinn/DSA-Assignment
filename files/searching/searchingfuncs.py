import math
from general.shortenfuncs import *
#Searching Functions

"""
Linear Search
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)

"""
def linearSearch(arr, target, mode):
    method = determine_type(mode)
    ind = {} #common sense search : looking through each of the items and comparing
    for i in range(len(arr)):
        if (isinstance(mode, int)):
            if (mode < 3):
                if (method(arr[i]) == target.upper()):
                    ind[i] = arr[i]
            else:
                if (method(arr[i]) == target):
                    ind[i] = arr[i]
        
        if (mode == 'listNum1'):
            if (arr[i].get_paxnum() >= target):
                ind[i] = arr[i]
                return ind
        elif (mode == 'listNum2'):
            if (arr[-(i+1)].get_paxnum() <= target):
                ind[-(i+1)] = arr[-(i+1)]
                return ind
        elif (mode == 'listCost1'):
            if (arr[i].get_packcost() >= target):
                ind[i] = arr[i]
                return ind #returning instantly shld get the next highest from the target
        elif (mode == 'listCost2'):
            if (arr[-(i+1)].get_packcost() <= target):
                ind[-(i+1)] = arr[-(i+1)]
                return ind #returning instantly shld get the next highest from the target
    
    return ind

"""
Binary Search
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))

"""
def binarySearch(arr,target,mode):
    method = determine_type(mode)
    ind = {}

    low = 0 # first index (pointer 1)
    high = len(arr) - 1 #last index (pointer 2)

    while (low <= high): #if low == then both pointers have met and search is complete
        mid = low + (high-low) // 2 #resetting mid when half is decided
        if (mode < 3):
            target = target.upper()

        if (method(arr[mid]) == target):
            ind = find_all_occurences(ind, mid, target, arr, method) #returns all occurences of target                
            return ind

        elif (method(arr[mid]) < target):
            low = mid + 1
        else:
            high = mid - 1

    return ind

"""
Jump Search

If left > length == index error , if arr[left] > val meaning the element you are trying to find is not present

if (arr[left].get_name().upper() <= val.upper()) and (arr[right].get_name().upper() >= val.upper()):
    break 
Break because the number should be in between the 2 but its not

left += jump 
else keep going untill its inbetween or the loop stops
"""
def JumpSearch(arr, val, mode):
    method = determine_type(mode)
    ind = {}
    #similar idea to shell sort, using increments
    #Only works on sorted list
    length = len(arr)
    jump = int(math.sqrt(length)) #Just a way of determining increments
    left, right = 0, 0
    if (mode < 3):
        val = val.upper()

    while (left < length) and (method(arr[left]) <= val):
        right = min(length - 1, left + jump)
        if (method(arr[left]) <= val) and (method(arr[right]) >= val):
            break
        left += jump

    right = min(length - 1, right)
    i = left
    while (i <= right) and (method(arr[i]) <= val):
        if (method(arr[i]) == val):
            ind = find_all_occurences(ind, i, val, arr, method)
        i += 1

    return ind

"""
Expo Search:
    Best time complexity: O(log(n))
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))

Helps find the range to use in Binary Search
Exponentially increases the index until the moment the index will return a value greater than the value

Then it will use binary search to find the item
"""
def ExponentialSearch(arr, val, mode):
    method = determine_type(mode)
    if (mode < 3):
        val = val.upper()
    
    if (method(arr[0]) == val):
        index = 0
        return binarySearch(arr[0:], val, mode)
    index = 1
    while (index < len(arr)) and (method(arr[index]) <= val):
        index = index * 2

    return binarySearch( arr[:min(index, len(arr))], val, mode)


"""
Fibonacci Search
    Best case: O(1) when the element to be found is the first element
    Worst case: O(log(n))
    Average case: O(log(n))

involves fibonacci sequence, the 3rd number is the sum of the 1st and second
uses fibonacci numbers to determine the block it searches
similar to binary search == divide and concur, but not equal split arrays and uses the +, - which is less costly on the cpu

What lines are for:
else :
    ind[i] = lys[i]
    Accomodate for duplicates, though does not really follow the Fibonnachi Search Logic.
    It basically loops and checks the left and right elements because its a sorted list and when its no longer what we want it breaks

i = min(index + fibM_minus_2, (len(lys)-1)) #avoiding index error using min()

"""
def FibonacciSearch(lys, val, mode):
    ind = {}
    method = determine_type(mode)
    fibM_minus_2 = 0 #(fibo(0))
    fibM_minus_1 = 1 #(fibo(1))
    fibM = fibM_minus_1 + fibM_minus_2 #(fibo(2))
    while (fibM < len(lys)): #finding the smallest fib number that is greater than or equal to the list
        fibM_minus_2 = fibM_minus_1 #(next fibo number)
        fibM_minus_1 = fibM #(fibo number)
        fibM = fibM_minus_1 + fibM_minus_2 #(next fibo number)
    index = -1
    if (mode < 3):
        val = val.upper()
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1)) #avoiding index error using min()

        '''
        if target is greater than element found, we move the index we start with in i to the one we just checked
        And check the elements afterwards, by changing the fibo numbers, so that we only deal with elements afterwards

        If target is lesser, we just lower the fibonacci numbers, so that we only deal with elements before the one we just checked
        '''
        if (method(lys[i]) < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (method(lys[i]) > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            ind = find_all_occurences(ind, i, val, lys, method)                
            return ind
        
        """
        To check last element, because while loop will break if fibM = 1
        """
        if (fibM_minus_1) and (method(lys[len(lys)-1]) == val):
            index = len(lys) - 1
            ind[index] = lys[index]

            while (True):
                index -= 1
                if (index < 0):
                    break
                if (method(lys[index]) == val):
                    ind[index] = lys[index]
                else:
                    break

            return ind 

    return ind
