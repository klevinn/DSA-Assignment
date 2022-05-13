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
    while (is_sorted(arr, mode) == False):
        shuffle(arr)

def bogo_search(array, target, mode):
    try:
        x = len(array) - 1
        i = 0

        if mode == 1:
            while array[i].get_name().upper() != target.upper():
                i = random.randint(0, x)
        elif mode == 2:
            while array[i].get_packname().upper() != target.upper():
                i = random.randint(0, x)
        elif mode == 3:
            while array[i] != target:
                i = random.randint(0, x)
        elif mode == 4:
            while array[i] != target:
                i = random.randint(0, x)
        return i
    except (KeyboardInterrupt):
        return -1  

#Stalin Sort
def stalinSort(arr):
    return [x for max_val in arr[:1] for x in arr if x >= max_val for max_val in (x,)]

def slow_sort(A, i, j):
	
	# Recursion break condition
	if (i >= j):
		return
		
	# Store the middle value
	m = (i + j) // 2
	
	# Recursively call with the
	# left half
	slow_sort(A, i, m)

	# Recursively call with the
	# right half
	slow_sort(A, m + 1, j)

	# Swap if the first element is
	# lower than second
	if (A[j] < A[m]):
		temp = A[m]
		A[m] = A[j]
		A[j] = temp

	# Recursively call with the
	# array excluding the maximum
	# element
	slow_sort(A, i, j - 1)
