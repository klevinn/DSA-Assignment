import dill #Persistent Storage
from tabulate import tabulate #Display of records

from records import Records
from sorting.sortingfuncs import *
from sorting.slowsortingfuncs import *
from searching.searchingfuncs import *
from tree.binarysearchtree import *

name = ["Wei Ren", "Eden", "Chung Wai", "Jabriel", "Joshua", "Clarence", "Jason", "Calvin"]
packs = {"Romance Package":300, "The Girls Getaway Package":500, "The Rest & Relaxation Package":325, "Staycation Package":250}

def create_random_record(): 
    #Initialising of Data, randomly set and return the object
    selectedName = random.choice(name)
    selectedPack = random.choice(list(packs.keys()))
    paxNum = random.randint(1,10)
    user = Records()
    user.set_name(selectedName)
    user.set_paxnum(paxNum)
    user.set_packcost(round(packs[selectedPack]/paxNum))
    user.set_packname(selectedPack)

    return user

#For searching of the Pack Name, getting the index of the key by creating a list of keys first
def get_packs_index(n):
    return list(packs)[n-1]

#Using the key obtained, putting it into the packs dictionary to get the cost associated with the name
#Do the math based of the number of people to get cost per pax
def get_packs_cost(pack, num):
    return round(packs[pack] / num)

#Persistent Storage Data
#Opening the Storage File
def open_pickles(): 
    #Try opening a record.pickle file if there
    try: 
        with open("record.pickle", "rb") as f:
            recordsList = dill.load(f)
    #If not found, create the list of people and create a pickle file wih it
    except IOError:
        recordsList = []
        for i in range(11):
            recordsList.append(create_random_record())
            rewrite_pickles(recordsList)
        

    return recordsList

#Rewriting the Storage File
def rewrite_pickles(obj):   
    #Just replacing the contents of the file
    with (open("record.pickle", "wb") as f):
        dill.dump(obj, f)

#Display Records
def display_records(db):
    #uses a module to display the records
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

#Same algorithm but changes due to the fact that Search results deal with dictionaries instead of lists
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
    #Additional functions for staff members
    additional = ["Add a Record", "Update a Record", "Delete a Record"]

    menu = [["Display all Records", "Records Settings", "Exit Application", "Return To Main Menu"],

    ["Sort record using Bubble sort", "Sort record using Selection sort", "Sort records using Insertion sort","Sort Records using Merge Sort","Sort Records using Quick Sort", "Sort Records using Counting Sort (Only Integers)", "Sort Records using Shell Sort", "Sort Records using Pancake Sort", "Sort Records using Comb Sort", "Sort Records using Cocktail Shaker Sort", "Sort Records using Tree Sort" ,"Sort Records using Heap Sort"],

    ["Search record using Linear Search and update record", "Search record using Binary Search and update record", "Search record using Jump Search and update record", "Search record using Fibonacci Search and update record", "Search record using Exponential Search and update record", "Search record using Binary Search Tree and update Record"],

    ["List records range from $X to $Y. e.g $100-200"]]


    #Exceptionally Slow sorts, for demonstration of Sorts NOT TO USE
    slowmenu = ["Sort using Bogo Sort", "Sort using Stalin Sort", "Sort using Slow Sort", "Sort using Sleep Sort", "Sort using Gnome Sort"]

    #Submenu to group all the sort, search and list functions
    submenu0 = ["Sort Records", "Search Records", "List Records"]
    #Sub Menus Just for different ways of sorts & search
    submenu = ["Sort by Customer Name", "Sort by Package Name", "Sort by Number of Pax", "Sort by Cost Per Pax"]
    submenu2 = ["Search by Customer Name", "Search by Package Name", "Search by Number of Pax", "Search by Cost Per Pax"]
    submenu3 = ["List by Pax Number", "List by Cost Per Pax"]

    #All menu stages look at the index of the item in the list, Consists of logs stored in dictionaries, where value is what will be displaye dwhen ran and the key is the input of the user
    #Logs also help with validation , as if the input not present in the logs, the code will not continue running and bring about an error

    #Stage 1 : The Main Menu. Asking Users if they want to display records, deal with records settings or Close Applicationd
    if (stage == 1):
        print("\n========= Menu =========\n")
        print("1.", menu[0][0])
        print("2.", menu[0][1])
        print("X.", menu[0][2])
        print("\n========================\n")
        return {1:"\nDisplaying Records...\n", "X":"\nExitting Application...\n", 2:"\nRecords Settings...\n", "EasterEgg":"\nDisplaying Easter Egg Sorts...\n"}
    
    #Stage 1.1 : The records settings menu , deals with adding records, update records & Deletion of records
    elif (stage == 1.1):
        print("\n========= Records Settings =========\n")
        print("1.", additional[0])
        print("2.", additional[1])
        print("3.", additional[2])
        print("X.", menu[0][3])
        print("\n========================\n")
        return {1:"\nAdding Records...\n", "X":"\nExitting Application...\n", 2:"\nUpdating a Record...\n", 3:"\nReturning To Main Menu...\n"}

    #Stage 2 : Displays all usable sorting algorithms
    elif (stage == 2):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n========= Menu Of Sorts =========\n")
        menunum = 1
        for i in menu[1]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSorting...\n"

            menunum += 1
        
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    #Stage 2.1 : Displays all Searching Algorithms
    elif (stage == 2.1):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n========= Menu Of Searches =========\n")
        menunum = 1
        for i in menu[2]:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSearching...\n"

            menunum += 1
        
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    #Stage 2.2: Displays all listing algorithms
    elif (stage == 2.2):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n========= Menu Of Listing =========\n")

        print("1.", menu[3][0])
        logs[1] = "\nListing...\n"
        
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs
    
    #Stage 3 : Displays the 4 ways of sorting (Name, Packname, Paxnum, packcost)
    elif (stage == 3):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n====== Sorting... ======\n")
        menunum = 1
        for i in submenu:
            print("%d." %(menunum), i)
            if (menunum == 1):
                logs[menunum] = "\nBy Customer Name...\n"
            elif (menunum == 2):
                logs[menunum] = "\nBy Package Name...\n"
            elif (menunum == 3):
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif (menunum == 4):
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    #Stage 3.1 = For Counting Sort, since they only deal with numbers, give them a menu that only shows the Number related options
    elif (stage == 3.1):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n====== Sorting... ======\n")
        menunum = 1
        for i in submenu[2:]:
            print("%d." %(menunum), i)
            if (menunum == 1):
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif (menunum == 2):
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs
    
    #Similar to stage 3
    #Stage 4 : Displays the 4 ways of searching (Name, Packname, Paxnum, packcost)
    elif (stage == 4):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n====== Searching... ======\n")
        menunum = 1
        for i in submenu2:
            print("%d." %(menunum), i)
            if (menunum == 1):
                logs[menunum] = "\nBy Customer Name...\n"
            elif (menunum == 2):
                logs[menunum] = "\nBy Package Name...\n"
            elif (menunum == 3):
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif (menunum == 4):
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    elif (stage == 4.1):
        logs = {"X":"\nReturning To Main Menu..\n"}
        print("\n====== Searching... ======\n")
        menunum = 1
        for i in submenu2[2:]:
            print("%d." %(menunum), i)
            if (menunum == 1):
                logs[menunum] = "\nBy Number Of Pax...\n"
            elif (menunum == 2):
                logs[menunum] = "\nBy Cost Per Pax...\n"
            
            menunum += 1

        # print("B.", "Return to Main Records Page")
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs
    
    #Stage 5: Displays the options, look at search / sort / list options
    elif (stage == 5):
        print("\n========= Menu =========\n")
        print("1.", submenu0[0])
        print("2.", submenu0[1])
        print("3.", submenu0[2])
        print("X.", menu[0][3])
        print("\n========================\n")
        return {1:"\nDisplaying Sorting Records Options...\n", 2:"\Displaying Searching Records Options...\n", 3:"\Displaying Listing Records Options...\n", "X":"\nReturning To Main Menu...\n"}

    #Special : For Easter egg Functions : never use ineffective sorts for listing
    elif (stage == 5.1):
        print("\n========= Menu =========\n")
        print("1.", submenu0[0])
        print("X.", menu[0][3])
        print("\n========================\n")
        return {1:"\nDisplaying Sorting Records Options...\n", "X":"\nReturning To Main Menu...\n"}

    #Special : Displaying of the ineffective sort options
    elif (stage == 6):
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n========= Menu =========\n")
        menunum = 1
        for i in slowmenu:
            print("%d." %(menunum) ,i)
            logs[menunum] = "\nSorting BUT SLOWLY...\n"

            menunum += 1
        
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    #For listing, displays the ways can list by
    elif stage == "list":
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n====== Listing... ======\n")
        menunum = 1
        for i in submenu3:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "Listing..."
            menunum += 1
        
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

    #Stage asc is to display the menu asking if the user wants it to bve descending or ascending order
    elif stage == "asc":
        logs = {"X":"\nReturning To Main Menu...\n"}
        print("\n====== Sorting... ======\n")
        submenu = ["By Ascending Order", "By Descending Order"]
        menunum =1
        for i in submenu:
            print("%d. %s" %(menunum, i))
            logs[menunum] = "%s..." %(i)
            menunum += 1
        
        # print("B.", "Return to Main Records Page")
        print("X.", menu[0][3])
        print("\n========================\n")

        return logs

#Displays the menu of Packages and their respective cost
def addmenu():
    menunum = 1
    print("\n==== Packages ====\n")
    for i in packs:
        print("%d. %s : $%.2f" %(menunum, i, packs[i]))
        menunum += 1

#Repeated Codes
def inputValue(question ,valid, logs):
    #Loop to ask questions till a valid response is stored
    while (valid):
        choice = input(question)
        try: 
            choice = int(choice)
            if (choice in logs):
                valid = 0
                print(logs[choice])
                
            else:
                print("Please enter either one of the options available")

        except:
            if (choice.upper() != "X"):
                print("Please enter either one of the options")
            else:
                print(logs[choice.upper()])
                return choice.upper()
    
    return choice

def question(question, valid, itype):
    while (valid):
        try:
            if (itype == "str"):
                x = input(question)
                return x
            elif (itype == "int" or itype == "int1"):
                x = int(input(question))
                return x
        except:
            if (itype == "int"):
                return ''
            print("Invalid Input")

def listing(valid):
    rang = []
    while (valid):
        choice = input("Enter first number for the range: ")
        try:
            choice = int(choice)
            rang.append(choice)
            break
        except:
            print("Please enter a number.")
        

    while (valid):
        choice2 = input("Enter second number for the range: ")
        try:
            choice2 = int(choice2)
            if (choice2 < choice):
                print("Please enter a number that is greater than the first number.")
            else:
                rang.append(choice2)
                break
        except:
            print("Please enter a number.")

    return rang

def listingFunc(db,valid, tertChoice):
    ranje = listing(valid)
    insertionSort(db,tertChoice+2,1)
    resultslist = []
    invalid = 0

    for i in range(len(ranje)):
        results = binarySearch(db,ranje[i],tertChoice+2)
        if (len(results) == 0) and (i == 0): #To find nearest number -- Using Linear Search to retrieve the next nearest index
            if tertChoice == 1:
                results = linearSearch(db, ranje[i],'listNum1')
            else:
                results = linearSearch(db, ranje[i],'listCost1')
        elif (len(results) == 0) and (i == 1):
            if tertChoice == 1:
                results = linearSearch(db, ranje[i],'listNum2')
            else:
                results = linearSearch(db, ranje[i],'listCost2')

            if (len(results) == 0):
                print("\n0 Results found!")
                print("Entered Range: %d-%d\n" %(ranje[0], ranje[1]))
                invalid = 1
            
            #Validate if results not present    
        resultslist.append(results)

    if (not invalid):
        lowestInd = min(resultslist[0])
        highestInd = max(resultslist[1])
        if (highestInd > 0):
            highestInd += 1
        elif (highestInd < 0):
            highestInd = None

        headers = ["Customer Name", "Package Name", "Number of Pax", "Cost per Pax(S$)"]
        data = []
        for i in db[lowestInd:highestInd]:
            var = []
            var.append(i.get_name())
            var.append(i.get_packname())
            var.append(i.get_paxnum())
            var.append(round(i.get_packcost()))
            data.append(var)
        
        print(tabulate(data, headers=headers, tablefmt="grid"))
        
        print("\nThere are %d results found! \n" %(len(data)))
        print("\nReturning to Main Page... \n")

def update_input(valid, question):
    while (valid):
        update = input(question)
        if (update.upper() == "Y") or (update.upper() == "N"):
            return update.upper()
        else:
            print("Please enter either (Y/N)")

def search(db, mode):
    valid = 1
    choice = inputValue("Which category would you like to search in? ",valid, menu(4))
    if (choice == 'X'):
        return 1
    #Choices 1 and 2 deal with String Inputs while 3 and 4 deal with numeric input
    elif (choice < 3):
        if (mode > 1) and (mode != 6): #Binary search tree is option 6, not needed sorting
            quickSort(db, 0, len(db)-1, choice, 1)
            print("\nThis Search Requires Sorting!\n")
            print("The Database will be sorted based on the category you searched by!")
            print("\nSort Complete!\n")

        keyword = question("Enter keyword: ", valid, "str")

        if (mode == 1):
            results = linearSearch(db,keyword,choice)
        elif (mode == 2):
            results = binarySearch(db,keyword,choice)
        elif (mode == 3):
            results = JumpSearch(db,keyword,choice)
        elif (mode == 4):
            results = FibonacciSearch(db,keyword,choice)
        elif (mode == 5):
            results = ExponentialSearch(db,keyword,choice)
        elif (mode == 6):
            tree = BSTCreate(db,choice)
            results = BSTsearch(tree, keyword.upper())

        if (len(results) != 0):
            
            display_records_search(results)

            if (len(results) == 1):
                valid = 1
                update = question("What would you like to update the name to? (Leave blank if not wanted): ", valid, "str")
                if (len(update) != 0):
                    if (choice == 1):
                        db[list(results.keys())[0]].set_name(update)
                        rewrite_pickles(db)
                        
                    elif (choice ==2):
                        db[list(results.keys())[0]].set_packname(update)
                        rewrite_pickles(db)


            else:
                valid = 1
                num = question("Use which row to indicate & Who would you like to edit? (Leave blank if not wanted): ", valid, "int")
                if (num == ''):
                    return 1
                update = question("What would you like to update the name to? (Leave blank if not wanted): ", valid, "str")
                if (len(update) != 0):
                    if (choice == 1):
                        db[list(results.keys())[num-1]].set_name(update)
                        rewrite_pickles(db)

                    elif (choice == 2):
                        db[list(results.keys())[num-1]].set_packname(update)
                        rewrite_pickles(db)

        else:
            print("\n\033[31;1m No Results Found\n")
            print("Keywords need to be exact. Entered Keyword: %s\033[0m" %(keyword))
            print("\nReturning to main page...\n")

    else:
        if (mode > 1) and (mode != 6):
            quickSort(db, 0, len(db)-1, choice, 1)
            print("\nThis Search Requires Sorting!\n")
            print("The Database will be sorted based on the category you searched by!")
            print("\nSort Complete!\n")

        keyword = question("Enter keyword: ", valid, "int1")

        if (mode == 1):
            results = linearSearch(db,keyword,choice)
        elif (mode == 2):
            results = binarySearch(db,keyword,choice)
        elif (mode == 3):
            results = JumpSearch(db,keyword,choice)
        elif (mode == 4):
            results = FibonacciSearch(db,keyword,choice)
        elif (mode == 5):
            results = ExponentialSearch(db,keyword,choice)
        elif (mode == 6):
            tree = BSTCreate(db,choice)
            results = BSTsearch(tree, keyword)

        if (len(results) != 0):
            
            display_records_search(results)

            if (len(results) == 1):
                valid = 1
                update = question("What would you like to update the number to? (Leave blank if not wanted): ", valid, "int")
                if (update != ''):
                    if (choice == 3):
                        db[list(results.keys())[0]].set_paxnum(update)
                        rewrite_pickles(db)

                    elif (choice == 4):
                        db[list(results.keys())[0]].set_packcost(update)
                        rewrite_pickles(db)

            else:
                valid = 1
                num = question("Who would you like to edit? (Use which row to indicate & Leave blank if not wanted): ", valid, "int")
                if (num == ''):
                    return 1
                update = question("What would you like to update the number to? (Leave blank if not wanted): ", valid, "int")
                if (update != ''):
                    if (choice == 3):
                        db[list(results.keys())[num-1]].set_paxnum(update)
                        rewrite_pickles(db)

                    elif (choice == 4):
                        db[list(results.keys())[num-1]].set_packcost(update)
                        rewrite_pickles(db)

        else:
            print("\n\033[31;1m No Results Found\n")
            print("Keywords need to be exact. Entered Keyword: %s\033[0m" %(keyword))
            print("\nReturning to main page...\n")
                    
                    
    return 1

def sorting(db, valid, mode):
    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
    if (asc == "X"):
        return
    if(mode == 6):
        choice = inputValue("What would you like to sort by? ",valid, menu(3.1))
    else:
        choice = inputValue("What would you like to sort by? ",valid, menu(3))
    if (choice == "X"):
        return

    if (mode == 1):
        bubbleSort(db,choice, asc)
    elif (mode == 2):
        selectionSort(db,choice,asc)
    elif (mode == 3):
        insertionSort(db,choice,asc)
    elif (mode == 4):
        db = mergeSort(db,choice, asc)
    elif (mode == 5):
        quickSort(db, 0, len(db)-1, choice, asc)
    elif (mode == 6):
        db = countingSort(db, choice, asc)
    elif (mode == 7):
        shellSort(db, choice, asc)
    elif (mode == 8):
        pancakeSort(db, choice, asc)
    elif (mode == 9):
        combsort(db, choice, asc)
    elif (mode == 10):
        db = cocktail_shaker_sort(db, choice, asc)
    elif (mode == 11):
        tree = BSTCreate(db,choice)
        db = treeSort(tree,[], asc)
    elif (mode == 12):
        heapSort(db, choice, asc)


    rewrite_pickles(db)

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
