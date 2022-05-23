import dill #Persistent Storage
from tabulate import tabulate
from records import Records
import random #Bogo Sort
import math #Jump Search

from binarytree import BSTsearch, BSTCreate

#Initialising Data, Test Data
name = ["Wei Ren", "Eden", "Chung Wai", "Jabriel", "Joshua", "Clarence", "Jason", "Calvin"]
packs = {"Romance Package":300, "The Girls Getaway Package":500, "The Rest & Relaxation Package":325, "Staycation Package":250}

def create_random_record(): #OOP
    selectedName = random.choice(name)
    selectedPack = random.choice(list(packs.keys()))
    paxNum = random.randint(1,10)
    user = Records()
    user.set_name(selectedName)
    user.set_paxnum(paxNum)
    user.set_packcost(round(packs[selectedPack]/paxNum))
    user.set_packname(selectedPack)

    return user

def get_packs_index(n):
    return list(packs)[n-1]

def get_packs_cost(pack, num):
    return round(packs[pack] / num)

#Persistent Storage Data

def open_pickles(): 
    try:
        with open("record.pickle", "rb") as f:
            recordsList = dill.load(f)
    except IOError:
        recordsList = []
        for i in range(11):
            recordsList.append(create_random_record())
            rewrite_pickles(recordsList)
        

    return recordsList

def rewrite_pickles(obj):   
    with open("record.pickle", "wb") as f:
        dill.dump(obj, f)

#Display Records

def display_records(db):
    headers = ["No.","Customer Name", "Package Name", "Number of Pax", "Cost per Pax(S$)"]
    data = []
    num = 1
    for i in db:
        var = []
        var.append(num)
        var.append(i.get_name())
        var.append(i.get_packname())
        var.append(i.get_paxnum())
        var.append(round(i.get_packcost()))
        data.append(var)
        num += 1
    
    print(tabulate(data, headers=headers, tablefmt="grid"))

def display_records_search(results):
    headers = ["No.","Customer Name", "Package Name", "Number of Pax", "Cost per Pax(S$)"]
    data = []
    num = 1
    for i in results.values():
        var = []
        var.append(num)
        var.append(i.get_name())
        var.append(i.get_packname())
        var.append(i.get_paxnum())
        var.append(round(i.get_packcost()))
        data.append(var)
        num += 1

    print(tabulate(data, headers=headers, tablefmt="grid"))

#Menu

def menu(stage): 
    #For menu
    additional = ["Add a Record", "Update a Record", "Delete a Record"]

    menu = ["Display all records", "Records Settings", "Sort record using Bubble sort", "Sort record using Selection sort", "Sort records using Insertion sort","Sort Records using Merge Sort","Sort Records using Quick Sort", "Sort Records using Counting Sort (Only Integers)", "Sort Records using Shell Sort", "Sort Records using Gnome Sort", "Sort Records using Comb Sort", "Sort Records using Cocktail Shaker Sort", "Sort Records using Tree Sort" ,"Sort Records using Heap Sort", "Search record using Linear Search and update record", "Search record using Binary Search and update record", "Search record using Jump Search and update record", "Search record using Fibonacci Search and update record(Single Occurence)", "Search record using Exponential Search and update record", "Search record using Binary Search Tree and update Record", "List records range from $X to $Y. e.g $100-200", "Exit Application" ]

    slowmenu = ["Sort using Bogo Sort", "Sort using Stalin Sort", "Sort using Slow Sort", "Search record using Bogo Search"]

    submenu0 = ["Sort Records", "Search Records", "List Records"]
    submenu = ["Sort by Customer Name", "Sort by Package Name", "Sort by Number of Pax", "Sort by Cost Per Pax"]
    submenu2 = ["Search by Customer Name", "Search by Package Name", "Search by Number of Pax", "Search by Cost Per Pax"]

    if stage == 1:
        print("\n========= Menu =========\n")
        print("1.", menu[0])
        print("2.", menu[1])
        print("X.", menu[21])
        print("\n========================\n")
        return {1:"\nDisplaying Records...\n", "X":"\nExitting Application...\n", 2:"\nRecords Settings...\n", "EasterEgg":"\nDisplaying Easter Egg Sorts...\n"}
    
    elif stage == 1.1:
        print("\n========= Records Settings =========\n")
        print("1.", additional[0])
        print("2.", additional[1])
        print("3.", additional[2])
        print("X.", menu[21])
        print("\n========================\n")
        return {1:"\nAdding Records...\n", "X":"\nExitting Application...\n", 2:"\nUpdating a Record...\n", 3:"\nDeleting a Record...\n"}

    elif stage == 2:
        logs = {"X":"\nExitting Application...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        for i in menu[2:14]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSorting...\n"

            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == 2.1:
        logs = {"X":"\nExitting Application...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        for i in menu[14:20]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSearching...\n"

            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == 2.2:
        logs = {"X":"\nExitting Application...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        for i in menu[20]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nListing...\n"

            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs
    
    elif stage == 3:
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Sorting... ======\n")
        menunum = 1
        for i in submenu:
            print("%d." %(menunum), i)
            if menunum == 1:
                logs[menunum] = "\nBy Customer Name...\n"
            elif menunum == 2:
                logs[menunum] = "\nBy Package Name...\n"
            elif menunum == 3:
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif menunum == 4:
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == 3.1:
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Sorting... ======\n")
        menunum = 1
        for i in submenu[2:]:
            print("%d." %(menunum), i)
            if menunum == 1:
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif menunum == 2:
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[21])
        print("\n========================\n")

        return logs
    
    elif stage == 4:
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Searching... ======\n")
        menunum = 1
        for i in submenu2:
            print("%d." %(menunum), i)
            if menunum == 1:
                logs[menunum] = "\nBy Customer Name...\n"
            elif menunum == 2:
                logs[menunum] = "\nBy Package Name...\n"
            elif menunum == 3:
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif menunum == 4:
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[21])
        print("\n========================\n")

        return logs
    
    elif stage == 5:
        print("\n========= Menu =========\n")
        print("1.", submenu0[0])
        print("2.", submenu0[1])
        print("3.", submenu0[2])
        print("X.", menu[21])
        print("\n========================\n")
        return {1:"\nDisplaying Sorting Records Options...\n", 2:"\Displaying Searching Records Options...\n", 3:"\Displaying Listing Records Options...\n", "X":"\nExitting Application...\n"}

    elif stage == 5.1:
        print("\n========= Menu =========\n")
        print("1.", submenu0[0])
        print("2.", submenu0[1])
        print("X.", menu[21])
        print("\n========================\n")
        return {1:"\nDisplaying Sorting Records Options...\n", 2:"\Displaying Searching Records Options...\n", "X":"\nExitting Application...\n"}

    #Special
    elif stage == 6:
        logs = {"X":"\nExitting Application...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        for i in slowmenu[:3]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSorting...\n"

            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == 6.1:
        logs = {"X":"\nExitting Application...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        print("%d." %(menunum), slowmenu[3])
        logs[menunum] = "\nSearching...\n"


        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == "list":
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Listing... ======\n")
        submenu = ["List by Pax Number", "List by Cost Per Pax"]
        menunum = 1
        for i in submenu:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "Listing..."
            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == "intsort":
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Sorting... ======\n")
        submenu = ["Sort by Pax Number", "Sort by Cost Per Pax"]
        menunum = 1
        for i in submenu:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "Sorting..."
            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs
    
    elif stage == "intsearch":
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Sorting... ======\n")
        submenu = ["Search by Pax Number", "Search by Cost Per Pax"]
        menunum = 1
        for i in submenu:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "Searching..."
            menunum += 1
        
        print("X.", menu[21])
        print("\n========================\n")

        return logs

    elif stage == "asc":
        logs = {"X":"\nExitting Application...\n"}
        print("\n====== Sorting... ======\n")
        submenu = ["By Ascending Order", "By Descending Order"]
        menunum =1
        for i in submenu:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "%s..." %(i)
            menunum += 1
        
        # print("B.", "Return to Main Records Page")
        print("X.", menu[21])
        print("\n========================\n")

        return logs

def addmenu():
    menunum = 1
    print("\n==== Packages ====\n")
    for i in packs:
        print("%d. %s : $%.2f" %(menunum, i, packs[i]))
        menunum += 1

#Extra functions for sorting Functions

#merge sort
def mergeSortedList(left, right, mode, rev):
    leftInd = 0
    rightInd = 0
    result = []
    
    if rev == 1:
        if mode == 1:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_name() < right[rightInd].get_name():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 2:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_packname() < right[rightInd].get_packname():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 3:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_paxnum() < right[rightInd].get_paxnum():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 4:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_packcost() < right[rightInd].get_packcost():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
    
    else:
        if mode == 1:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_name() > right[rightInd].get_name():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 2:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_packname() > right[rightInd].get_packname():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 3:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_paxnum() > right[rightInd].get_paxnum():
                    result.append(left[leftInd])
                    leftInd += 1
                else:
                    result.append(right[rightInd])
                    rightInd += 1
        elif mode == 4:
            while leftInd < len(left) and rightInd < len(right): #Basically comparing each value and appending to list if greater or smaller
                if left[leftInd].get_packcost() > right[rightInd].get_packcost():
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

    for j in range(low, high): #comparing all list elements with the pivot
        if rev == 1:
            if mode == 1:
                if array[j].get_name() <= pivot.get_name():  #if element is smaller, swap with the greater element
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 2:
                if array[j].get_packname() <= pivot.get_packname():  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 3:
                if array[j].get_paxnum() <= pivot.get_paxnum():  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 4:
                if array[j].get_packcost() <= pivot.get_packcost():  
                    i += 1
                    array[i], array[j] = array[j], array[i]
        else:
            if mode == 1:
                if array[j].get_name() >= pivot.get_name(): 
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 2:
                if array[j].get_packname() >= pivot.get_packname():  
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 3:
                if array[j].get_paxnum() >= pivot.get_paxnum():
                    i += 1
                    array[i], array[j] = array[j], array[i]
            elif mode == 4:
                if array[j].get_packcost() >= pivot.get_packcost():  
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

#Sorting Functions

def bubbleSort(arr, mode, rev):
    n = len(arr)
    for _ in range(n):
        for i in range(n-1): #minus 1 because don't want out of range error
            if mode == 1:
                if rev == 1:
                    if arr[i].get_name() > arr[i+1].get_name(): #if previous variable greater than next variable  swap the 2
                        arr[i], arr[i+1] = arr[i+1], arr[i] #no need of storing temp variable
                else:
                    if arr[i].get_name() < arr[i+1].get_name():
                        arr[i], arr[i+1] = arr[i+1], arr[i]    
            elif mode == 2:
                if rev == 1:
                    if arr[i].get_packname() > arr[i+1].get_packname():
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if arr[i].get_packname() < arr[i+1].get_packname():
                        arr[i], arr[i+1] = arr[i+1], arr[i]
            elif mode == 3:
                if rev == 1:
                    if arr[i].get_paxnum() > arr[i+1].get_paxnum():
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if arr[i].get_paxnum() < arr[i+1].get_paxnum():
                        arr[i], arr[i+1] = arr[i+1], arr[i]                   
            elif mode == 4:
                if rev == 1:
                    if arr[i].get_packcost() > arr[i+1].get_packcost():
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if arr[i].get_packcost() < arr[i+1].get_packcost():
                        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    
    return arr

def selectionSort(arr, mode, rev):
    n = len(arr)
    for i in range(n):
        lowest = i
        for j in range(i+1,n):
            if mode == 1:
                if rev == 1:
                    if arr[j].get_name() < arr[lowest].get_name():
                        lowest = j
                else:
                    if arr[j].get_name() > arr[lowest].get_name():
                        lowest = j
            if mode == 2:
                if rev == 1:
                    if arr[j].get_packname() < arr[lowest].get_packname():
                        lowest = j
                else:
                    if arr[j].get_packname() > arr[lowest].get_packname():
                        lowest = j
            if mode == 3:
                if rev == 1:
                    if arr[j].get_paxnum() < arr[lowest].get_paxnum():
                        lowest = j
                else:
                    if arr[j].get_paxnum() > arr[lowest].get_paxnum():
                        lowest = j
            if mode == 4:
                if rev == 1:
                    if arr[j].get_packcost() < arr[lowest].get_packcost():
                        lowest = j
                else:
                    if arr[j].get_packcost() > arr[lowest].get_packcost():
                        lowest = j
    
        arr[i], arr[lowest] = arr[lowest], arr[i]
    
    return arr

def insertionSort(arr, mode, rev):
    n = len(arr)
    for i in range(1, n): #start from 1 due to checking with previous value and -1 will return the wrong number
        value = arr[i]
        current = i

        if mode == 1:
            if rev == 1:
                while current > 0 and arr[current-1].get_name() > value.get_name():
                    arr[current] = arr[current-1] #Swaps the 2
                    current -= 1 #As the while loop goes on, it keeps checking if value is smaller and swaps with the backwards
            else:
                while current > 0 and arr[current-1].get_name() < value.get_name():
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif mode == 2:
            if rev == 1:
                while current > 0 and arr[current-1].get_packname() > value.get_packname():
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while current > 0 and arr[current-1].get_packname() < value.get_packname():
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif mode == 3:
            if rev == 1:
                while current > 0 and arr[current-1].get_paxnum() > value.get_paxnum():
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while current > 0 and arr[current-1].get_paxnum() < value.get_paxnum():
                    arr[current] = arr[current-1] 
                    current -= 1 
        elif mode == 4:
            if rev == 1:
                while current > 0 and arr[current-1].get_packcost() > value.get_packcost():
                    arr[current] = arr[current-1] 
                    current -= 1 
            else:
                while current > 0 and arr[current-1].get_packcost() < value.get_packcost():
                    arr[current] = arr[current-1] 
                    current -= 1 
        
        arr[current] = value #When the loop stops running, places the value at its correct index

    return arr

def mergeSort(arr, mode, rev):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2

        lefthalf = mergeSort(arr[:mid], mode, rev)
        righthalf = mergeSort(arr[mid:], mode, rev)

        newList = mergeSortedList(lefthalf, righthalf, mode, rev)

        return newList

def quickSort(array, low, high, mode, rev):
    if low < high:
        pi = partition(array, low, high, mode, rev) #find pivot where left side is smaller and ride side is greater

        #sorting left side and right side again respectively
        quickSort(array, low, pi - 1, mode, rev) #left side
        quickSort(array, pi + 1, high, mode, rev) #right side

def countingSort(array, mode, rev):
    size = len(array)
    output = [0] * size
    newarr = []
    for i in range(len(array)):
        if mode == 1:
            newarr.append(array[i].get_paxnum())
        else:
            newarr.append(array[i].get_packcost())
    greatest = max(newarr)

    # Initialize count array
    count = [0] * (greatest + 1)

    # Store the count of each elements in count array
    for i in range(0, size):
        if mode == 1:
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
    if rev == 1:
        while i >= 0:
            if mode == 1:
                output[count[array[i].get_paxnum()] - 1] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[count[array[i].get_packcost()] - 1] = array[i]
                count[array[i].get_packcost()] -= 1

            i -= 1

    else:
        #Descending
        while i >= 0:
            if mode == 1:
                output[-(count[array[i].get_paxnum()])] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[-(count[array[i].get_packcost()])] = array[i]
                count[array[i].get_packcost()] -= 1
            
            i -= 1

    return output

def shellSort(array, mode, rev):

    n = len(array)

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):          
            temp = array[i]
            j = i
            if rev == 1:
                if mode == 1:
                    while j >= interval and array[j - interval].get_name() > temp.get_name():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 2:
                    while j >= interval and array[j - interval].get_packname() > temp.get_packname():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 3:
                    while j >= interval and array[j - interval].get_paxnum() > temp.get_paxnum():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 4:
                    while j >= interval and array[j - interval].get_packcost() > temp.get_packcost():
                        array[j] = array[j - interval]
                        j -= interval
            
            else:
                if mode == 1:
                    while j >= interval and array[j - interval].get_name() < temp.get_name():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 2:
                    while j >= interval and array[j - interval].get_packname() < temp.get_packname():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 3:
                    while j >= interval and array[j - interval].get_paxnum() < temp.get_paxnum():
                        array[j] = array[j - interval]
                        j -= interval

                elif mode == 4:
                    while j >= interval and array[j - interval].get_packcost() < temp.get_packcost():
                        array[j] = array[j - interval]
                        j -= interval

            array[j] = temp

        interval //= 2

def gnomeSort(arr, mode , rev):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index += 1

        if rev == 1:
            if mode == 1:
                if arr[index].get_name() >= arr[index - 1].get_name():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 2:
                if arr[index].get_packname() >= arr[index - 1].get_packname():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 3:
                if arr[index].get_paxnum() >= arr[index - 1].get_paxnum():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 4:
                if arr[index].get_packcost() >= arr[index - 1].get_packcost():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
        else:
            if mode == 1:
                if arr[index].get_name() <= arr[index - 1].get_name():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 2:
                if arr[index].get_packname() <= arr[index - 1].get_packname():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 3:
                if arr[index].get_paxnum() <= arr[index - 1].get_paxnum():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            elif mode == 4:
                if arr[index].get_packcost() <= arr[index - 1].get_packcost():
                    index += 1
                else:
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
            
    return arr

def combsort(arr, mode, rev):
    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(arr) - gap):
            j = i+gap

            if rev == 1:
                if mode == 1:
                    if arr[i].get_name() > arr[j].get_name():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 2:
                    if arr[i].get_packname() > arr[j].get_packname():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 3:
                    if arr[i].get_paxnum() > arr[j].get_paxnum():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 4:
                    if arr[i].get_packcost() > arr[j].get_packcost():
                        arr[i], arr[j] = arr[j], arr[i]   
                        swaps = True
            else:
                if mode == 1:
                    if arr[i].get_name() < arr[j].get_name():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 2:
                    if arr[i].get_packname() < arr[j].get_packname():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 3:
                    if arr[i].get_paxnum() < arr[j].get_paxnum():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True
                elif mode == 4:
                    if arr[i].get_packcost() < arr[j].get_packcost():
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps = True

def cocktail_shaker_sort(nums, mode, rev):
    for i in range(len(nums)-1, 0, -1):
        is_swapped = False
        
        if rev == 1:
            if mode == 1:
                for j in range(i, 0, -1):
                    if nums[j].get_name() < nums[j-1].get_name():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_name() > nums[j+1].get_name():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 2:
                for j in range(i, 0, -1):
                    if nums[j].get_packname() < nums[j-1].get_packname():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_packname() > nums[j+1].get_packname():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 3:
                for j in range(i, 0, -1):
                    if nums[j].get_paxnum() < nums[j-1].get_paxnum():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_paxnum() > nums[j+1].get_paxnum():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 4:
                for j in range(i, 0, -1):
                    if nums[j].get_packcost() < nums[j-1].get_packcost():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_packcost() > nums[j+1].get_packcost():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True
        
        else:
            if mode == 1:
                for j in range(i, 0, -1):
                    if nums[j].get_name() > nums[j-1].get_name():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_name() < nums[j+1].get_name():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 2:
                for j in range(i, 0, -1):
                    if nums[j].get_packname() > nums[j-1].get_packname():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_packname() < nums[j+1].get_packname():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 3:
                for j in range(i, 0, -1):
                    if nums[j].get_paxnum() > nums[j-1].get_paxnum():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_paxnum() < nums[j+1].get_paxnum():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True

            elif mode == 4:
                for j in range(i, 0, -1):
                    if nums[j].get_packcost() > nums[j-1].get_packcost():
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        is_swapped = True

                for j in range(i):
                    if nums[j].get_packcost() < nums[j+1].get_packcost():
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swapped = True
        
        if not is_swapped:
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

#Searching Functions

def linearSearch(arr, target, mode):
    ind = {} #common sense search : looking through each of the items and comparing
    for i in range(len(arr)):
        if mode == 1:
            if arr[i].get_name().upper() == target.upper():
                ind[i] = arr[i]
        elif mode == 2:
            if arr[i].get_packname().upper() == target.upper():
                ind[i] = arr[i]
        elif mode == 3:
            if arr[i].get_paxnum() == target:
                ind[i] = arr[i]
        elif mode == 4:
            if arr[i].get_packcost() == target:
                ind[i] = arr[i]            
        elif mode == 'listNum1':
            if arr[i].get_paxnum() > target:
                ind[i] = arr[i]
                return ind
        elif mode == 'listNum2':
            if arr[-(i+1)].get_paxnum() < target:
                ind[-(i+1)] = arr[-(i+1)]
                return ind
        elif mode == 'listCost1':
            if arr[i].get_packcost() > target:
                ind[i] = arr[i]
                return ind #returning instantly shld get the next highest from the target
        elif mode == 'listCost2':
            if arr[-(i+1)].get_packcost() < target:
                ind[-(i+1)] = arr[-(i+1)]
                return ind #returning instantly shld get the next highest from the target
    
    return ind

def binarySearch(arr,target,mode):
    ind = {}

    low = 0 # first index (pointer 1)
    high = len(arr) - 1 #last index (pointer 2)

    while low <= high: #if low == then both pointers have met and search is complete
        mid = low + (high-low) // 2 #resetting mid when half is decided

        if mode == 1:
            if arr[mid].get_name().upper() == target.upper():
                ind[mid] = arr[mid]
                low = mid + 1 #check through the rest for duplicates
            elif arr[mid].get_name().upper() < target.upper():
                low = mid + 1 
            else:
                high = mid - 1
        elif mode == 2:
            if arr[mid].get_packname().upper() == target.upper():
                ind[mid] = arr[mid]
                low = mid + 1
            elif arr[mid].get_packname().upper() < target.upper():
                low = mid + 1 
            else:
                high = mid - 1
        elif mode == 3:
            if arr[mid].get_paxnum() == target:
                ind[mid] = arr[mid]
                low = mid + 1    
            elif arr[mid].get_paxnum() < target:
                low = mid + 1 
            else:
                high = mid - 1
        elif mode == 4:
            if arr[mid].get_packcost() == target:
                ind[mid] = arr[mid]
                low = mid + 1       
            elif arr[mid].get_packcost() < target:
                low = mid + 1 
            else:
                high = mid - 1

    return ind

def JumpSearch(arr, val, mode):
    ind = {}

    #Only works on sorted list
    length = len(arr)
    jump = int(math.sqrt(length)) #Just a way of determining increments
    left, right = 0, 0

    if mode == 1:
        while left < length and arr[left].get_name().upper() <= val.upper(): #If left > length == index error , if arr[left] > val meaning the element you are trying to find is not present
            right = min(length - 1, left + jump)
            if arr[left].get_name().upper() <= val.upper() and arr[right].get_name().upper() >= val.upper():
                break #Break because the number would be in between the 2 
            left += jump #else keep going untill its inbetween or the loop stops
        
        # if left >= length or arr[left].get_name() > val:
        #     return -1

        right = min(length - 1, right)
        i = left
        while i <= right and arr[i].get_name().upper() <= val.upper(): #left needs to be smallerr than right
            if arr[i].get_name().upper() == val.upper():
                ind[i] = arr[i]
            i += 1

    elif mode == 2:
        while left < length and arr[left].get_packname().upper() <= val.upper():
            right = min(length - 1, left + jump)
            if arr[left].get_packname().upper() <= val.upper() and arr[right].get_packname().upper() >= val.upper():
                break 
            left += jump 

        # if left >= length or arr[left].get_packname() > val:
        #     return -1

        right = min(length - 1, right)
        i = left
        while i <= right and arr[i].get_packname().upper() <= val.upper(): 
            if arr[i].get_packname().upper() == val.upper():
                ind[i] = arr[i]
            i += 1
    
    elif mode == 3:
        while left < length and arr[left].get_paxnum() <= val:
            right = min(length - 1, left + jump)
            if arr[left].get_paxnum() <= val and arr[right].get_paxnum() >= val:
                break 
            left += jump
        
        # if left >= length or arr[left].get_paxnum() > val:
        #     return -1

        right = min(length - 1, right)
        i = left
        while i <= right and arr[i].get_paxnum() <= val: 
            if arr[i].get_paxnum() == val:
                ind[i] = arr[i]
            i += 1

    elif mode == 4:
        while left < length and arr[left].get_packcost() <= val:
            right = min(length - 1, left + jump)
            if arr[left].get_packcost() <= val and arr[right].get_packcost() >= val:
                break 
            left += jump
        
        # if left >= length or arr[left].get_packcost() > val:
        #     return -1

        right = min(length - 1, right)
        i = left
        while i <= right and arr[i].get_packcost() <= val: 
            if arr[i].get_packcost() == val:
                ind[i] = arr[i]
            i += 1

    return ind

def ExponentialSearch(arr, val, mode):
    if mode == 1:
        if arr[0].get_name().upper() == val.upper():
            return 0
        index = 1
        while index < len(arr) and arr[index].get_name().upper() <= val.upper():
            index = index * 2
    elif mode == 2:
        if arr[0].get_packname().upper() == val.upper():
            return 0
        index = 1
        while index < len(arr) and arr[index].get_packname().upper() <= val.upper():
            index = index * 2
    elif mode == 3:
        if arr[0].get_paxnum() == val:
            return 0
        index = 1
        while index < len(arr) and arr[index].get_paxnum() <= val:
            index = index * 2
    elif mode == 4:
        if arr[0].get_packcost() == val:
            return 0
        index = 1
        while index < len(arr) and arr[index].get_packcost() <= val:
            index = index * 2

    return binarySearch( arr[:min(index, len(arr))], val, mode)

#Only single occurence // fix soon
def FibonacciSearch(lys, val, mode):
    ind = {}
#involves fibonacci sequence
# uses fibonacci numbers to determine the block it searches
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)): #finding the smallest fib number that is greater than or equal to the list
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if mode == 1:
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
                #Accomodate for duplicates
                j = i
                original = lys[i]
                while True:
                    i += 1
                    if lys[i].get_name() == original.get_name():
                        ind[i] = lys[i]
                    else:
                        break
                
                while True:
                    j -= 1
                    if lys[j].get_name() == original.get_name():
                        ind[j] = lys[j]
                    else:
                        break
                    
                return ind
            
            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_name().upper() == val.upper()):
                ind[index+1] = lys[index+1]
                return ind

        if mode == 2:
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
                return ind
                
            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_packname().upper() == val.upper()):
                ind[index+1] = lys[index+1]
                return ind

        if mode == 3:
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
                return ind

            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_paxnum() == val):
                ind[index+1] = lys[index+1]
                return ind

        if mode == 4:
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
                return ind

            if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1].get_packcost() == val):
                ind[index+1] = lys[index+1]
                return ind

#Repeated Codes -- Simplified to Functions

def inputValue(question ,valid, logs):
    while valid:
        choice = input(question)
        try: 
            choice = int(choice)
            if choice in logs:
                valid = 0
                print(logs[choice])
                
            else:
                print("Please enter either one of the options available")

        except:
            if choice.upper() != "X":
                print("Please enter either one of the options")
            else:
                print(logs[choice.upper()])
                return "X"
    
    return choice

def question(question, valid, itype):
    while valid:
        try:
            if itype == "str":
                x = input(question)
                return x
            elif itype == "int":
                x = int(input(question))
                return x
        except:
            if itype == "int":
                return ''
            print("Invalid Input")

def listing(valid):
    rang = []
    while valid:
        choice = input("Enter first number for the range: ")
        try:
            choice = int(choice)
            rang.append(choice)
            break
        except:
            print("Please enter a number.")
        

    while valid:
        choice2 = input("Enter second number for the range: ")
        try:
            choice2 = int(choice2)
            if choice2 < choice:
                print("Please enter a number that is greater than the first number.")
            else:
                rang.append(choice2)
                break
        except:
            print("Please enter a number.")

    return rang

def update_input(valid, question):
    while valid:
        update = input(question)
        if update.upper() == "Y" or update.upper() == "N":
            return update.upper()
        else:
            print("Please enter either (Y/N)")

def search(db, mode):
    valid = 1
    choice = inputValue("Which category would you like to search in? ",valid, menu(4))
    if choice == 'X':
        return 1
    elif choice < 3:
        if mode > 1 and mode != 6:
            new = insertionSort(db,choice, 1)
            print("\nThis Search Requires Sorting!\n")
            print("The Database will be sorted based on the category you searched by!")
            print("\nSort Complete!\n")

        keyword = question("Enter keyword: ", valid, "str")

        if mode == 1:
            results = linearSearch(db,keyword,choice)
        elif mode == 2:
            results = binarySearch(new,keyword,choice)
        elif mode == 3:
            results = JumpSearch(new,keyword,choice)
        elif mode == 4:
            results = FibonacciSearch(new,keyword,choice)
        elif mode == 5:
            results = ExponentialSearch(new,keyword,choice)
        elif mode == 6:
            tree = BSTCreate(db,choice)
            results = BSTsearch(tree, keyword.upper())

        if len(results) != 0:
            
            display_records_search(results)

            if len(results) == 1:
                valid = 1
                update = question("What would you like to update the name to? (Leave blank if not wanted): ", valid, "str")
                if len(update) != 0:
                    if choice == 1:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[0]].set_name(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[0]].set_name(update)
                            rewrite_pickles(new)                            
                    elif choice ==2:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[0]].set_packname(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[0]].set_packname(update)
                            rewrite_pickles(new)

            else:
                valid = 1
                num = question("Use which row to indicate & Who would you like to edit? (Leave blank if not wanted): ", valid, "int")
                if num == '':
                    return 1
                update = question("What would you like to update the name to? (Leave blank if not wanted): ", valid, "str")
                if len(update) != 0:
                    if choice == 1:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[num-1]].set_name(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[num-1]].set_name(update)
                            rewrite_pickles(new)
                    elif choice == 2:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[num-1]].set_packname(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[num-1]].set_packname(update)
                            rewrite_pickles(new)
        else:
            print("\nNo Results Found\n")
            print("Keywords need to be exact. Entered Keyword: %s" %(keyword))
            print("\nReturning to main page...\n")

    else:
        if mode > 1 and mode != 6:
            new = insertionSort(db,choice, 1)
            print("\nThis Search Requires Sorting!\n")
            print("The Database will be sorted based on the category you searched by!")
            print("\nSort Complete!\n")
        keyword = question("Enter keyword: ", valid, "int")

        if mode == 1:
            results = linearSearch(db,keyword,choice)
        elif mode == 2:
            results = binarySearch(new,keyword,choice)
        elif mode == 3:
            results = JumpSearch(new,keyword,choice)
        elif mode == 4:
            results = FibonacciSearch(new,keyword,choice)
        elif mode == 5:
            results = ExponentialSearch(new,keyword,choice)
        elif mode == 6:
            tree = BSTCreate(db,choice)
            results = BSTsearch(tree, keyword)

        if len(results) != 0:
            
            display_records_search(results)

            if len(results) == 1:
                valid = 1
                update = question("What would you like to update the number to? (Leave blank if not wanted): ", valid, "int")
                if update != '':
                    if choice == 3:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[0]].set_paxnum(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[0]].set_paxnum(update)
                            rewrite_pickles(new)
                    elif choice == 4:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[0]].set_packcost(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[0]].set_packcost(update)
                            rewrite_pickles(new)
            else:
                valid = 1
                num = question("Who would you like to edit? (Use which row to indicate & Leave blank if not wanted): ", valid, "int")
                if num == '':
                    return 1
                update = question("What would you like to update the number to? (Leave blank if not wanted): ", valid, "int")
                if update != '':
                    if choice == 3:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[num-1]].set_paxnum(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[num-1]].set_paxnum(update)
                            rewrite_pickles(new)
                    elif choice == 4:
                        if mode == 1 or mode == 6:
                            db[list(results.keys())[num-1]].set_packcost(update)
                            rewrite_pickles(db)
                        else:
                            new[list(results.keys())[num-1]].set_packcost(update)
                            rewrite_pickles(new)
        else:
            print("\nNo Results Found\n")
            print("Keywords need to be exact. Entered Keyword: %s" %(keyword))
            print("\nReturning to main page...\n")
                    
                    
    return 1

