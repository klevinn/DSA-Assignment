import random

#BogoSort

#To check if array is sorted or Not
def is_sorted(a, mode):
    n = len(a)
    for i in range(0, n-1):
        if (mode == 1):
            if (a[i].get_name() > a[i+1].get_name()): #Checking if previous element is greater than the next one
                return False #If greater == not sorted (ascendingly) hence return false
        if (mode == 2):
            if (a[i].get_packname() > a[i+1].get_packname()): 
                return False 
        if (mode == 3):
            if (a[i].get_paxnum() > a[i+1].get_paxnum()): 
                return False 
        if (mode == 4):
            if (a[i].get_packcost() > a[i+1].get_packcost()): 
                return False 
    return True

#To generate permutation of an array
def shuffle(arr):
    n = len(arr)
    for i in range(0,n):
        r = random.randint(0,n-1) #GEnerates a random number and swaps with the i
        arr[i], arr[r] = arr[r], arr[i]

def bogoSort(arr, mode):
    i = 1
    while (is_sorted(arr, mode) == False):
        shuffle(arr)
        print("Sort %d : Unsuccessful" %(i), end="\r")
        i += 1
    
    print("Sort %d : Successful" %(i))


# def bogo_search(array, target, mode):
#     try:
#         x = len(array) - 1
#         i = 0

#         if (mode == 1):
#             while (array[i].get_name().upper() != target.upper()):
#                 i = random.randint(0, x)
#         elif (mode == 2):
#             while (array[i].get_packname().upper() != target.upper()):
#                 i = random.randint(0, x)
#         elif (mode == 3):
#             while (array[i] != target):
#                 i = random.randint(0, x)
#         elif (mode == 4):
#             while (array[i] != target):
#                 i = random.randint(0, x)
#         return i
#     except (KeyboardInterrupt):
#         return -1  

#Stalin Sort
def stalinSort(arr, mode):
    #Need redo
    pass

def slow_sort(A, i, j, mode, rev):
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
        if (mode == 1):
            if (A[j].get_name() < A[m].get_name()):
                A[m] , A[j] = A[j], A[m]
        
        elif (mode == 2):
            if (A[j].get_packname() < A[m].get_packname()):
                A[m] , A[j] = A[j], A[m]

        elif (mode == 3):
            if (A[j].get_paxnum() < A[m].get_paxnum()):
                A[m] , A[ j] = A[j], A[m]

        elif (mode == 4):
            if (A[j].get_packcost() < A[m].get_packcost()):
                A[m] , A[j] = A[j], A[m]
    
    else:
        if (mode == 1):
            if (A[j].get_name() > A[m].get_name()):
                A[m] , A[j] = A[j], A[m]
        
        elif (mode == 2):
            if (A[j].get_packname() > A[m].get_packname()):
                A[m] , A[j] = A[j], A[m]

        elif (mode == 3):
            if (A[j].get_paxnum() > A[m].get_paxnum()):
                A[m] , A[j] = A[j], A[m]

        elif (mode == 4):
            if (A[j].get_packcost() > A[m].get_packcost()):
                A[m] , A[j] = A[j], A[m]
    
    slow_sort(A, i, j-1, mode, rev)