import random
from time import sleep
from threading import Timer
from functions import inputValue, menu, update_input, rewrite_pickles
#BogoSort

#To check if array is sorted or Not
def is_sorted(a, mode, rev):
    n = len(a)
    for i in range(0, n-1):
        if (rev == 1):
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
        else:
            if (mode == 1):
                if (a[i].get_name() < a[i+1].get_name()): #Checking if previous element is greater than the next one
                    return False #If greater == not sorted (ascendingly) hence return false
            if (mode == 2):
                if (a[i].get_packname() < a[i+1].get_packname()): 
                    return False 
            if (mode == 3):
                if (a[i].get_paxnum() < a[i+1].get_paxnum()): 
                    return False 
            if (mode == 4):
                if (a[i].get_packcost() < a[i+1].get_packcost()): 
                    return False 
    return True

#To generate permutation of an array
def shuffle(arr):
    n = len(arr)
    for i in range(0,n):
        r = random.randint(0,n-1) #GEnerates a random number and swaps with the i
        arr[i], arr[r] = arr[r], arr[i]

def bogoSort(arr, mode, rev):
    i = 1
    while (is_sorted(arr, mode, rev) == False):
        shuffle(arr)
        print("Sort %d : Unsuccessful" %(i), end="\r")
        i += 1
    
    print("Sort %d : Successful" %(i))

#Stalin Sort
def stalinSort(arr, mode, rev):
    if (len(arr) < 1):
        return arr
    val = arr[0]
    newarr = []
    for i in arr:
        if (rev == 1):
            if (mode == 1):
                if (i.get_name() >= val.get_name()):
                    newarr.append(i)
                    val = i

            elif (mode == 2):
                if (i.get_packname() >= val.get_packname()):
                    newarr.append(i)
                    val = i

            elif (mode == 3):
                if (i.get_paxnum() >= val.get_paxnum()):
                    newarr.append(i)
                    val = i

            elif (mode == 4):
                if (i.get_packcost() >= val.get_packcost()):
                    newarr.append(i)
                    val = i
        else:
            if (mode == 1):
                if (i.get_name() <= val.get_name()):
                    newarr.append(i)
                    val = i

            elif (mode == 2):
                if (i.get_packname() <= val.get_packname()):
                    newarr.append(i)
                    val = i

            elif (mode == 3):
                if (i.get_paxnum() <= val.get_paxnum()):
                    newarr.append(i)
                    val = i

            elif (mode == 4):
                if (i.get_packcost() <= val.get_packcost()):
                    newarr.append(i)
                    val = i   
    
    return newarr

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




def sleep_sort(arr, mode, rev):
    result = []
    def add1(x):
        result.append(x)

    ind = arr[0]
    for i in arr:
        if (rev == 1):
            if (mode == 1):
                if (ind.get_paxnum() < i.get_paxnum()): ind = i
                Timer(i.get_paxnum(), add1, [i]).start()
            else:
                if (ind.get_packcost() < i.get_packcost()): ind = i
                Timer(i.get_packcost(), add1, [i]).start()
        else:
            if (mode == 1):
                if (ind.get_paxnum() > i.get_paxnum()): ind = i
                Timer(i.get_paxnum(), add1, [i]).start()
            else:
                if (ind.get_packcost() > i.get_packcost()): ind = i
                Timer(i.get_packcost(), add1, [i]).start()

    if (mode == 1):
        sleep(ind.get_paxnum()+1)
    elif (mode == 2):
        sleep(ind.get_packcost()+1)
    
    return result

def gnomeSort(arr, mode , rev):
    #improved insertion sort
    n = len(arr)
    index = 0
    while (index < n):
        if (index == 0):
            index += 1

        if (rev == 1):
            if (mode == 1):
                if (arr[index].get_name() >= arr[index - 1].get_name()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 2):
                if (arr[index].get_packname() >= arr[index - 1].get_packname()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 3):
                if (arr[index].get_paxnum() >= arr[index - 1].get_paxnum()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 4):
                if (arr[index].get_packcost() >= arr[index - 1].get_packcost()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
        else:
            if (mode == 1):
                if (arr[index].get_name() <= arr[index - 1].get_name()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 2):
                if (arr[index].get_packname() <= arr[index - 1].get_packname()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 3):
                if (arr[index].get_paxnum() <= arr[index - 1].get_paxnum()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif (mode == 4):
                if (arr[index].get_packcost() <= arr[index - 1].get_packcost()):
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1

def slow_sorting(db, valid, mode):
    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
    if (asc == "X"):
        return
    if(mode == 4):
        choice = inputValue("What would you like to sort by? ",valid, menu(3.1))
    else:
        choice = inputValue("What would you like to sort by? ",valid, menu(3))
    if (choice == "X"):
        return

    if (mode == 1):
        try:
            bogoSort(db,choice, asc)
        except (KeyboardInterrupt):
            print("Took too long to Sort. Welcome to O(Infinity)")

    elif (mode == 2):
        upd = update_input(valid, "This sort may remove elements from the list. Are you sure you want to do this? (Y/N)")
        if (upd == "X"):
            return
    
        db = stalinSort(db, choice, asc)

    elif (mode == 3):

        slow_sort(db, 0 , len(db)-1, choice, asc)

    elif (mode == 4):

        db = sleep_sort(db,choice,asc)

    elif (mode == 5):

        gnomeSort(db, choice, asc)
    
    rewrite_pickles(db)