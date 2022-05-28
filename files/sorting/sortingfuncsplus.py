#File for extra functions needed in Sort Functions

#merge sort
def mergeSortedList(left, right, mode, rev):
    leftInd = 0
    rightInd = 0
    result = []
    
    #First initiate a whileloop that will end once an out of range error will occur (one of the saved variables of the index exceed te length)
    """
    As he loop goes through they will compare the values of thee element of each list
    If the value is lesser than, the element will be appended first, and the index they are checking will add 1
    Then this process will go through untill the while condition is reached.

    Since its possible for there to be leftover elements in the list. After the while loop we add anything remaining into the result from the index that breaks the while loop

    First pass (Looking at both index 0): 
    Left - [1,5,6,7,9]
    Right - [2,3,4,8]
    
    IDE sees 1 is lesser than 2:
    FinalArr - [1]

    Second Pass (Looking at left index 1 and right index 0):
    IDE sees 2 is lesser than 5
    FinalArr - [1,2]

    Third Pass (Looks at left index 1 and right index 1):
    ...
    
    """

    if (rev == 1):
        if (mode == 1):
            while (leftInd < len(left)) and (rightInd < len(right)): 
                if (left[leftInd].get_name() < right[rightInd].get_name()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 2):
            while (leftInd < len(left)) and (rightInd < len(right)): 
                if (left[leftInd].get_packname() < right[rightInd].get_packname()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 3):
            while (leftInd < len(left)) and (rightInd < len(right)):
                if (left[leftInd].get_paxnum() < right[rightInd].get_paxnum()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 4):
            while (leftInd < len(left)) and (rightInd < len(right)):
                if (left[leftInd].get_packcost() < right[rightInd].get_packcost()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
    
    else:
        if (mode == 1):
            while (leftInd < len(left)) and (rightInd < len(right)): 
                if (left[leftInd].get_name() > right[rightInd].get_name()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 2):
            while (leftInd < len(left)) and (rightInd < len(right)):
                if (left[leftInd].get_packname() > right[rightInd].get_packname()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 3):
            while (leftInd < len(left)) and (rightInd < len(right)): 
                if (left[leftInd].get_paxnum() > right[rightInd].get_paxnum()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif (mode == 4):
            while (leftInd < len(left)) and (rightInd < len(right)):
                if (left[leftInd].get_packcost() > right[rightInd].get_packcost()):
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1        

    result += left[leftInd:]
    result += right[rightInd:]
    return result

#quick sort
def partition(array, low, high, mode, rev):
    pivot = array[high] #last element is pivot value
    i = low - 1 # pointer for greater element

    for j in range(low, high): #comparing all list elements between the pivot
        if (rev == 1):
            if (mode == 1):
                if (array[j].get_name() <= pivot.get_name()):  #if element is smaller, swap with the greater element
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 2):
                if (array[j].get_packname() <= pivot.get_packname()):  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 3):
                if (array[j].get_paxnum() <= pivot.get_paxnum()):  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 4):
                if (array[j].get_packcost() <= pivot.get_packcost()):  
                    i += 1
                    array[i], array[j] = array[j], array[i]
        else:
            if (mode == 1):
                if (array[j].get_name() >= pivot.get_name()): 
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 2):
                if (array[j].get_packname() >= pivot.get_packname()):  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 3):
                if (array[j].get_paxnum() >= pivot.get_paxnum()):
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif (mode == 4):
                if (array[j].get_packcost() >= pivot.get_packcost()):  
                    i += 1
                    array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1

#heap sort
def heapify(arr, n, i, mode, rev):

#Order of elements is the level order traversal of the tree

#Build max heap by swapping the root with the node (higher node on top)

    # Find largest among root and children
    largest = i #greatest index placed into the heapify()

    #since its a complete binary tree, where the order of elements in an array is the level order traversal of the tree. the left and right subtree of the root is always decided by a set formula
    l = 2 * i + 1 #Left node of the root (i) 
    r = 2 * i + 2 #right node of the root (i)

    if rev == 1:
        if mode == 1:
        #checking if the element suppsoed to be in the left tree exists, if more than len means doesnt exist
        #checking if the subtree node is greater, if greater the element number takes the largest
            if l < n and arr[i].get_name() < arr[l].get_name():
                largest = l

            #checkign right element if exists, and checking if right element is greater than the left element if exists
            if r < n and arr[largest].get_name() < arr[r].get_name():
                largest = r

        elif mode == 2:
            if l < n and arr[i].get_packname() < arr[l].get_packname():
                largest = l

            if r < n and arr[largest].get_packname() < arr[r].get_packname():
                largest = r
        
        elif mode == 3:
            if l < n and arr[i].get_paxnum() < arr[l].get_paxnum():
                largest = l

            if r < n and arr[largest].get_paxnum() < arr[r].get_paxnum():
                largest = r
        
        elif mode == 4:
            if l < n and arr[i].get_packcost() < arr[l].get_packcost():
                largest = l

            if r < n and arr[largest].get_packcost() < arr[r].get_packcost():
                largest = r
    else:
        if mode == 1:
        #checking if the element suppsoed to be in the left tree exists, if more than len means doesnt exist
        #checking if the subtree node is lesser, if lesser the element number takes the largest
            if l < n and arr[i].get_name() > arr[l].get_name():
                largest = l

            #checkign right element if exists, and checking if right element is lesser than the left element if exists
            if r < n and arr[largest].get_name() > arr[r].get_name():
                largest = r

        elif mode == 2:
            if l < n and arr[i].get_packname() > arr[l].get_packname():
                largest = l

            if r < n and arr[largest].get_packname() > arr[r].get_packname():
                largest = r
        
        elif mode == 3:
            if l < n and arr[i].get_paxnum() > arr[l].get_paxnum():
                largest = l

            if r < n and arr[largest].get_paxnum() > arr[r].get_paxnum():
                largest = r
        
        elif mode == 4:
            if l < n and arr[i].get_packcost() > arr[l].get_packcost():
                largest = l

            if r < n and arr[largest].get_packcost() > arr[r].get_packcost():
                largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest,mode, rev) #to ensure that the nodes new position, is still the max heap

#pancake sort
# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while (start < i):
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

# Returns index of the maximum
# element in arr
def findMax(arr, n, mode, rev):
    maxindex = 0
    for i in range(0,n):
        if (rev == 1):
            if (mode == 1):
                if (arr[i].get_name() > arr[maxindex].get_name()):
                    maxindex = i
            elif (mode == 2):
                if (arr[i].get_packname() > arr[maxindex].get_packname()):
                    maxindex = i
            elif (mode == 3):
                if (arr[i].get_paxnum() > arr[maxindex].get_paxnum()):
                    maxindex = i
            elif (mode == 4):
                if (arr[i].get_packcost() > arr[maxindex].get_packcost()):
                    maxindex = i
        else:
            if (mode == 1):
                if (arr[i].get_name() < arr[maxindex].get_name()):
                    maxindex = i
            elif (mode == 2):
                if (arr[i].get_packname() < arr[maxindex].get_packname()):
                    maxindex = i
            elif (mode == 3):
                if (arr[i].get_paxnum() < arr[maxindex].get_paxnum()):
                    maxindex = i
            elif (mode == 4):
                if (arr[i].get_packcost() < arr[maxindex].get_packcost()):
                    maxindex = i
    
    return maxindex
