import random

#BogoSort

#To check if array is sorted or Not
def is_sorted(a, mode):
    n = len(a)
    for i in range(0, n-1):
        if mode == 1:
            if (a[i].get_name() > a[i+1].get_name()): #Checking if previous element is greater than the next one
                return False #If greater == not sorted (ascendingly) hence return false
        if mode == 2:
            if (a[i].get_packname() > a[i+1].get_packname()): 
                return False 
        if mode == 3:
            if (a[i].get_paxnum() > a[i+1].get_paxnum()): 
                return False 
        if mode == 4:
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
    n = len(arr)
    while (is_sorted(arr, mode) == False):
        shuffle(arr)
    

#Stalin Sort
def stalinSort(arr):
    return [x for max_val in arr[:1] for x in arr if x >= max_val for max_val in (x,)]


