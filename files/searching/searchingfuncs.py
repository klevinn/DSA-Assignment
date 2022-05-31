import math
from general.shortenfuncs import *
#Searching Functions

"""
Linear Search


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
            if (arr[i].get_paxnum() > target):
                ind[i] = arr[i]
                return ind
        elif (mode == 'listNum2'):
            if (arr[-(i+1)].get_paxnum() < target):
                ind[-(i+1)] = arr[-(i+1)]
                return ind
        elif (mode == 'listCost1'):
            if (arr[i].get_packcost() > target):
                ind[i] = arr[i]
                return ind #returning instantly shld get the next highest from the target
        elif (mode == 'listCost2'):
            if (arr[-(i+1)].get_packcost() < target):
                ind[-(i+1)] = arr[-(i+1)]
                return ind #returning instantly shld get the next highest from the target
    
    return ind

"""
Binary Search


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

        if (method(arr[mid]) == target): #if mid is the target
            ind[mid] = arr[mid]
            low = mid + 1
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
Break because the number would be in between the 2 
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
        print(val)

    while (left < length) and (method(arr[left]) <= val):
        right = min(length - 1, left + jump)
        if (method(arr[left]) <= val) and (method(arr[right]) >= val):
            break
        left += jump

    right = min(length - 1, right)
    i = left
    while (i <= right) and (method(arr[i]) <= val):
        if (method(arr[i]) == val):
            ind[i] = arr[i]
        i += 1

    return ind

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

involves fibonacci sequence, the 3rd number is the sum of the 1st and second
uses fibonacci numbers to determine the block it searches
similar to binary search == divide and concur, but not equal split arrays and uses the +, - which is less costly on the cpu

else :
    ind[i] = lys[i]
    Accomodate for duplicates, though does not really follow the Fibonnachi Search Logic.
    It basically loops and checks the left and right elements because its a sorted list and when its no longer what we want it breaks

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
        i = min(index + fibM_minus_2, (len(lys)-1))

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
            ind[i] = lys[i]
            j = i
            original = lys[i]
            while (True):
                i += 1
                if (i > len(lys)):
                    break
                if (method(lys[i]) == method(original)):
                    ind[i] = lys[i]
                else:
                    break
            
            while (True):
                j -= 1
                if (j < 0):
                    break
                if (method(lys[j]) == method(original)):
                    ind[j] = lys[j]
                else:
                    break
                
            return ind
        
        if(fibM_minus_1 and index < (len(lys)-1) and method(lys[index+1]) == val):
            index += 1
            ind[index] = lys[index]
            while (True):
                index += 1
                if (index > len(lys)):
                    break
                if (method(lys[index]) == val):
                    ind[index] = lys[index]
                else:
                    break
            return ind    

    return ind
