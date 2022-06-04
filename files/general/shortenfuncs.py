def determine_type(mode):
    method = '' #Just to avoid unbound local
    
    if (mode == 1):
        method = lambda x: x.get_name().upper()
    elif (mode == 2):
        method = lambda x: x.get_packname().upper()
    elif (mode == 3):
        method = lambda x: x.get_paxnum()
    elif (mode == 4):
        method = lambda x: x.get_packcost()
    
    return method

"""
Checks to the left and right of the found item 

If found any items, appended to the results dictionary, if not breaks from loop
"""

def find_all_occurences(ind, mid, target, arr, method):
    ind[mid] = arr[mid]
    j = mid
    while (True):
        mid += 1
        if (mid >= len(arr)):
            break
        if (method(arr[mid]) == target):
            ind[mid] = arr[mid]
        else:
            break
    
    while (True):
        j -= 1
        if (j < 0):
            break
        if (method(arr[j]) == target):
            ind[j] = arr[j]
        else:
            break
    
    return ind
