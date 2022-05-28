import math
#Searching Functions

def linearSearch(arr, target, mode):
    ind = {} #common sense search : looking through each of the items and comparing
    for i in range(len(arr)):
        if (mode == 1):
            if (arr[i].get_name().upper() == target.upper()):
                ind[i] = arr[i] #Accomodate for duplicates, however sacrifice on time complexity as needs to go through the entire list
        elif (mode == 2):
            if (arr[i].get_packname().upper() == target.upper()):
                ind[i] = arr[i]
        elif (mode == 3):
            if (arr[i].get_paxnum() == target):
                ind[i] = arr[i]
        elif (mode == 4):
            if (arr[i].get_packcost() == target):
                ind[i] = arr[i]            
        elif (mode == 'listNum1'):
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

def binarySearch(arr,target,mode):
    ind = {}

    low = 0 # first index (pointer 1)
    high = len(arr) - 1 #last index (pointer 2)

    while (low <= high): #if low == then both pointers have met and search is complete
        mid = low + (high-low) // 2 #resetting mid when half is decided

        if (mode == 1):
            if (arr[mid].get_name().upper() == target.upper()):
                ind[mid] = arr[mid] #Same as linear search, accomodats for dupes but sacrifices time complexity
                low = mid + 1 #check through the rest for duplicates
            elif (arr[mid].get_name().upper() < target.upper()):
                low = mid + 1 
            else:
                high = mid - 1
        elif (mode == 2):
            if (arr[mid].get_packname().upper() == target.upper()):
                ind[mid] = arr[mid]
                low = mid + 1
            elif (arr[mid].get_packname().upper() < target.upper()):
                low = mid + 1 
            else:
                high = mid - 1
        elif (mode == 3):
            if (arr[mid].get_paxnum() == target):
                ind[mid] = arr[mid]
                low = mid + 1    
            elif (arr[mid].get_paxnum() < target):
                low = mid + 1 
            else:
                high = mid - 1
        elif (mode == 4):
            if (arr[mid].get_packcost() == target):
                ind[mid] = arr[mid]
                low = mid + 1       
            elif (arr[mid].get_packcost() < target):
                low = mid + 1 
            else:
                high = mid - 1

    return ind

def JumpSearch(arr, val, mode):
    ind = {}
    #similar idea to shell sort, using increments
    #Only works on sorted list
    length = len(arr)
    jump = int(math.sqrt(length)) #Just a way of determining increments
    left, right = 0, 0

    if (mode == 1):
        while (left < length) and (arr[left].get_name().upper() <= val.upper()): #If left > length == index error , if arr[left] > val meaning the element you are trying to find is not present
            right = min(length - 1, left + jump)
            if (arr[left].get_name().upper() <= val.upper()) and (arr[right].get_name().upper() >= val.upper()):
                break #Break because the number would be in between the 2 
            left += jump #else keep going untill its inbetween or the loop stops
        

        right = min(length - 1, right)
        i = left
        while (i <= right) and (arr[i].get_name().upper() <= val.upper()): #left needs to be smallerr than right
            if (arr[i].get_name().upper() == val.upper()):
                ind[i] = arr[i]
            i += 1

    elif (mode == 2):
        while (left < length) and (arr[left].get_packname().upper() <= val.upper()):
            right = min(length - 1, left + jump)
            if (arr[left].get_packname().upper() <= val.upper()) and (arr[right].get_packname().upper() >= val.upper()):
                break 
            left += jump 

        right = min(length - 1, right)
        i = left
        while (i <= right) and (arr[i].get_packname().upper() <= val.upper()): 
            if (arr[i].get_packname().upper() == val.upper()):
                ind[i] = arr[i]
            i += 1
    
    elif (mode == 3):
        while (left < length) and (arr[left].get_paxnum() <= val):
            right = min(length - 1, left + jump)
            if (arr[left].get_paxnum() <= val) and (arr[right].get_paxnum() >= val):
                break 
            left += jump
        
        right = min(length - 1, right)
        i = left
        while (i <= right) and (arr[i].get_paxnum() <= val): 
            if (arr[i].get_paxnum() == val):
                ind[i] = arr[i]
            i += 1

    elif (mode == 4):
        while (left < length) and (arr[left].get_packcost() <= val):
            right = min(length - 1, left + jump)
            if (arr[left].get_packcost() <= val) and (arr[right].get_packcost() >= val):
                break 
            left += jump
        
        right = min(length - 1, right)
        i = left
        while (i <= right) and (arr[i].get_packcost() <= val): 
            if (arr[i].get_packcost() == val):
                ind[i] = arr[i]
            i += 1

    return ind

def ExponentialSearch(arr, val, mode):
    #Index goes up
    if (mode == 1):
        if (arr[0].get_name().upper() == val.upper()):
            return 0
        index = 1
        while (index < len(arr)) and (arr[index].get_name().upper() <= val.upper()):
            index = index * 2
    elif (mode == 2):
        if (arr[0].get_packname().upper() == val.upper()):
            return 0
        index = 1
        while (index < len(arr)) and (arr[index].get_packname().upper() <= val.upper()):
            index = index * 2
    elif (mode == 3):
        if (arr[0].get_paxnum() == val):
            return 0
        index = 1
        while (index < len(arr)) and (arr[index].get_paxnum() <= val):
            index = index * 2
    elif (mode == 4):
        if (arr[0].get_packcost() == val):
            return 0
        index = 1
        while (index < len(arr)) and (arr[index].get_packcost() <= val):
            index = index * 2

    return binarySearch( arr[:min(index, len(arr))], val, mode)

def FibonacciSearch(lys, val, mode):
    ind = {}
#involves fibonacci sequence, the 3rd number is the sum of the 1st and second
# uses fibonacci numbers to determine the block it searches
# similar to binary search == divide and concur, but not equal split arrays and uses the +, - which is less costly on the cpu
    fibM_minus_2 = 0 #(fibo(0))
    fibM_minus_1 = 1 #(fibo(1))
    fibM = fibM_minus_1 + fibM_minus_2 #(fibo(2))
    while (fibM < len(lys)): #finding the smallest fib number that is greater than or equal to the list
        fibM_minus_2 = fibM_minus_1 #(next fibo number)
        fibM_minus_1 = fibM #(fibo number)
        fibM = fibM_minus_1 + fibM_minus_2 #(next fibo number)
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (mode == 1):
            if (lys[i].get_name().upper() < val.upper()):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (lys[i].get_name().upper() > val.upper()):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                ind[i] = lys[i]
                #Accomodate for duplicates, though does not really follow the Fibonnachi Search Logic.
                #It basically loops and checks the left and right elements because its a sorted list and when its no longer what we want it breaks
                j = i
                original = lys[i]
                while (True):
                    i += 1
                    if (lys[i].get_name() == original.get_name()):
                        ind[i] = lys[i]
                    else:
                        break
                
                while (True):
                    j -= 1
                    if (lys[j].get_name() == original.get_name()):
                        ind[j] = lys[j]
                    else:
                        break
                    
                return ind
            
            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_name().upper() == val.upper()):
                index += 1
                ind[index] = lys[index]
                while (True):
                    index += 1
                    if (lys[index].get_name().upper() == val.upper()):
                        ind[index] = lys[index]
                    else:
                        break
                return ind

        if (mode == 2):
            if (lys[i].get_packname().upper() < val.upper()):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (lys[i].get_packname().upper() > val.upper()):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                ind[i] = lys[i]

                j = i
                original = lys[i]
                while (True):
                    i += 1
                    if (lys[i].get_packname() == original.get_packname()):
                        ind[i] = lys[i]
                    else:
                        break
                
                while (True):
                    j -= 1
                    if (lys[j].get_packname() == original.get_packname()):
                        ind[j] = lys[j]
                    else:
                        break

                return ind
                
            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_packname().upper() == val.upper()):
                index += 1
                ind[index] = lys[index]
                while (True):
                    index += 1
                    if (lys[index].get_packname().upper() == val.upper()):
                        ind[index] = lys[index]
                    else:
                        break
                return ind

        if (mode == 3):
            if (lys[i].get_paxnum() < val):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (lys[i].get_paxnum() > val):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                ind[i] = lys[i]

                j = i
                original = lys[i]
                while (True):
                    i += 1
                    if (lys[i].get_paxnum() == original.get_paxnum()):
                        ind[i] = lys[i]
                    else:
                        break
                
                while (True):
                    j -= 1
                    if (lys[j].get_paxnum() == original.get_paxnum()):
                        ind[j] = lys[j]
                    else:
                        break

                return ind

            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_paxnum() == val):
                index+=1
                ind[index] = lys[index]
                while (True):
                    index += 1
                    if (lys[index].get_paxnum() == val):
                        ind[index] = lys[index]
                    else:
                        break
                return ind

        if (mode == 4):
            if (lys[i].get_packcost() < val):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (lys[i].get_packcost() > val):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                ind[i] = lys[i]

                j = i
                original = lys[i]
                while (True):
                    i += 1
                    if lys[i].get_packcost() == original.get_packcost():
                        ind[i] = lys[i]
                    else:
                        break
                
                while (True):
                    j -= 1
                    if lys[j].get_packcost() == original.get_packcost():
                        ind[j] = lys[j]
                    else:
                        break

                return ind

            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_packcost() == val):
                index += 1
                ind[index] = lys[index]
                while (True):
                    index += 1
                    if lys[index].get_packcost() == val:
                        ind[index] = lys[index]
                    else:
                        break
                return ind
    
    return ind
