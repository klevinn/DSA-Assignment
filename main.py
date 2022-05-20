#modules
from tabulate import tabulate
import time

from records import Records
from functions import display_records, get_packs_index, get_packs_cost, open_pickles, rewrite_pickles, menu, addmenu, bubbleSort, selectionSort, insertionSort, mergeSort, search, linearSearch, binarySearch,  inputValue, question, listing, quickSort, countingSort, update_input, shellSort, gnomeSort, combsort, cocktail_shaker_sort

from binarytree import BSTCreate

from slowsortfuncs import bogoSort, bogo_search, stalinSort, slow_sort

#Extras to be done : Design (Color Codes)

#Functions to be done : Heap Sort (O(n log n)), Shell Sort, Gnome Sort, comb sort, cocktail shaker sort.  Maybe 1 more search algo, Table Algorithm, must be useful (so check for time complexity), Do the return to previous page, Validate supposed to be number only input can enter letters (pax num in search)

#Search Funcs: https://stackabuse.com/search-algorithms-in-python/
#Possible : Fibonnachi Search #CODES DONE JUST NOT IMPLEMENTED

#Binary Search Tree

#Maybe Functions : CubeSort O(n log n)

#Fun Functions : Bogo Sort / Bozo Sort : o(infinity), slow sort, sleep sort, stalin sort, bogo search

#Dropped, Why : RaditzSort (Only good time complexity when large amount of data), shell sort (overall bad time complexity), Intrapolation Search (No use of implementation),  Tim Sort, Intra Sort, (Involves merge / quick no extra marks involved)

#Done: All Basic Features to get a passing grade, Counting Sort, Additonal Features for administrators (Add, Remove, Update), Jump Search, Exponential Search,

def main():
    choice = ""
    while choice != "X":
        db = open_pickles()
        valid = 1
        print("Successful Running...")

        while valid: #Validation for User Inputs
            logs = menu(1)
            choice = input("What would you like to do? ")
            try: 
                choice = int(choice)
                if choice > 2:
                    print("Please enter either a valid option")
                else:
                    print(logs[choice])
                    valid = 0
                    time.sleep(0.2)

            except:
                if choice.upper() == "X":
                    print(logs[choice.upper()])
                    return
                elif choice in logs:
                    print(logs[choice])
                    valid = 0
                else:
                    print("Please enter a valid option")
                

        #Main records page
        if choice == 1:
            #input pagination for Records
            #Hardcode table after done with sorting algos
            display_records(db)

            valid = 1
            choice = inputValue("What would you like to do? ", valid, menu(5))
            
            #Sorting
            if choice == 1:

                display_records(db)

                valid = 1
                choice = inputValue("What would you like to do? ", valid, menu(2))

                #Bubble Sort Code O(n^2)
                if choice == 1:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue

                    new = bubbleSort(db,choice, asc)
                    rewrite_pickles(new)

                    continue
                
                #Selection Sort Code O(n^2)
                elif choice == 2:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue

                    new = selectionSort(db,choice, asc)
                    rewrite_pickles(new)

                    continue
                
                #Insertion Sort Code O(n^2)
                elif choice == 3:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue

                    new = insertionSort(db,choice, asc)
                    rewrite_pickles(new)
                    continue
                
                #Merge Sort Code O(n log n)
                elif choice == 4:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue

                    new = mergeSort(db,choice, asc)
                    rewrite_pickles(new)
                    continue
                
                #Quick Sort Code O(n^2)
                elif choice == 5:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue

                    quickSort(db, 0, len(db)-1, choice, asc)
                    rewrite_pickles(db)
                    continue
                
                #Counting Sort O(n+k)
                elif choice == 6:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu("intsort")) #Remember to remove option for name and package name
                    if choice == "X":
                        continue

                    new = countingSort(db, choice, asc)
                    rewrite_pickles(new)
                    continue
                
                #Shell Sort
                elif choice == 7:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3)) #Remember to remove option for name and package name
                    if choice == "X":
                        continue

                    shellSort(db, choice, asc)
                    rewrite_pickles(db)

                    continue
                
                #Gnome Sort
                elif choice == 8:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3)) #Remember to remove option for name and package name
                    if choice == "X":
                        continue

                    new = gnomeSort(db, choice, asc)
                    rewrite_pickles(new)

                    continue
                
                #Comb Sort
                elif choice == 9:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3)) #Remember to remove option for name and package name
                    if choice == "X":
                        continue

                    combsort(db, choice, asc)
                    rewrite_pickles(db)

                    continue
                
                #Cocktail Shaker Sort
                elif choice == 10:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3)) #Remember to remove option for name and package name
                    if choice == "X":
                        continue

                    new = cocktail_shaker_sort(db, choice, asc)
                    rewrite_pickles(new)

                    continue

            #Searching
            elif choice == 2:
                
                display_records(db)

                valid = 1
                choice = inputValue("What would you like to do? ", valid, menu(2.1))

                #Linear Search Code
                if choice == 1:
                    
                    rez = search(db, choice)
                    if rez:
                        continue
                
                #Binary Search Code
                elif choice == 2:

                    rez = search(db, choice)
                    if rez:
                        continue
                
                #Jump Search Code
                elif choice == 3:

                    rez = search(db, choice)
                    if rez:
                        continue
                
                #Fibonacci Search Code (NOT DONE) 
                elif choice == 4:

                    rez = search(db,choice)
                    if rez == '':
                        continue
                
                #Exponential Search Code
                elif choice == 5:

                    rez = search(db,choice)
                    if rez == '':
                        continue
                
                #BST Code
                elif choice == 6:
                    rez = search(db,choice)
                    if rez == '':
                        continue
            #Listing
            elif choice == 3:

                display_records(db)

                valid = 1
                choice = inputValue("What would you like to do? ", valid, menu(2.2))
            
            #List Code (Using both Linear & Binary Search)
                if choice == 1:
                    valid = 1
                    choice = inputValue("What would you like to do? ", valid, menu("list"))
                    if choice == "X":
                        continue
                    elif choice == 1:
                        mode = 3
                        ranje = listing(valid)
                        new = insertionSort(db,mode,1)

                        resultslist = []
                        invalid = 0

                        for i in range(len(ranje)):
                            results = binarySearch(new,ranje[i],mode)

                            if len(results) == 0 and i == 0: #To find nearest number -- Using Linear Search to retrieve the next nearest index
                                results = linearSearch(new, ranje[i],'listNum1')
                            elif len(results) == 0 and i == 1:
                                results = linearSearch(new, ranje[i],'listNum2')
                                if len(results) == 0:
                                    print("\n0 Results found!")
                                    print("Entered Range: %d-%d\n" %(ranje[0], ranje[1]))
                                    invalid = 1
                                
                                #Validate if results not present    
                            resultslist.append(results)
                        
                        if not invalid:
                            lowestInd = min(resultslist[0])
                            highestInd = max(resultslist[1]) #Never factor in that user can enter a value not present in table / Binary search might not be best idea
                            
                            if highestInd > 0:
                                highestInd += 1

                            headers = ["Customer Name", "Package Name", "Number of Pax", "Cost per Pax(S$)"]
                            data = []
                            for i in new[lowestInd:highestInd]:
                                var = []
                                var.append(i.get_name())
                                var.append(i.get_packname())
                                var.append(i.get_paxnum())
                                var.append(round(i.get_packcost()))
                                data.append(var)
                            
                            print(tabulate(data, headers=headers, tablefmt="grid"))
                            
                            print("\nThere are %d results found! \n" %(len(data)))
                            print("\nReturning to Main Page... \n")

                    elif choice == 2:
                        mode = 4
                        ranje = listing(valid)
                        new = insertionSort(db,mode,1)

                        resultslist = []
                        invalid = 0

                        for i in range(len(ranje)):
                            results = binarySearch(new,ranje[i],mode)

                            if len(results) == 0 and i == 0:
                                results = linearSearch(new, ranje[i],'listCost1')
                            elif len(results) == 0 and i == 1:
                                results = linearSearch(new, ranje[i],'listCost2')
                                if len(results) == 0:
                                    print("\n0 Results found!")
                                    print("Entered Range: %d-%d\n" %(ranje[0], ranje[1]))
                                    invalid = 1
                            
                            resultslist.append(results)
                    
                        if not invalid:
                            lowestInd = min(resultslist[0])
                            highestInd = max(resultslist[1]) 

                            if highestInd > 0:
                                highestInd += 1

                            headers = ["Customer Name", "Package Name", "Number of Pax", "Cost per Pax(S$)"]
                            data = []
                            for i in new[lowestInd:highestInd]:
                                var = []
                                var.append(i.get_name())
                                var.append(i.get_packname())
                                var.append(i.get_paxnum())
                                var.append(round(i.get_packcost()))
                                data.append(var)
                            
                            print(tabulate(data, headers=headers, tablefmt="grid"))
                            
                            print("\nThere are %d results found! \n" %(len(data)))
                            print("\nReturning to Main Page... \n")

                    continue

        #Records Settings pahe
        elif choice == 2:
            
            valid = 1
            choice = inputValue("What would you like to do? ", valid, menu(1.1))

            #Adding a Record
            if choice == 1:
                valid = 1
                obj = Records()
                name = input("Name: ")
                while valid:
                    addmenu()
                    package = input("\nChoose 1 of the packages: ")
                    try:
                        package = int(package)
                        if package > 4 or package < 1:
                            print("Please enter a valid option")
                        else:
                            break
                    except:
                        print("Please enter a valid option")
                
                package = get_packs_index(package)

                while valid:
                    try:
                        paxnum = int(input("\nHow many people?: "))
                        break
                    except:
                        print("Please enter a valid number")

                packcost = get_packs_cost(package, paxnum)
                obj.set_name(name)
                obj.set_packname(package)
                obj.set_paxnum(paxnum)
                obj.set_packcost(packcost)

                db.append(obj)
                rewrite_pickles(db)

                continue
        
            #Update Record
            elif choice == 2:
                
                display_records(db)

                update = 0
                valid = 1
                while valid:
                    try:
                        num = int(input("Which record would you like to update? "))
                        if num > len(db):
                            print("Please enter an EXISTING record")
                        else:
                            break
                    except:
                        print("Please enter a valid number")

                new = db[num-1]

                #Name Update
                print("Name : %s" %(new.get_name()))
                upd = update_input(valid, "Would you like to update the name?(Y/N) ")
                if upd == "Y":
                    name = input("Enter the new name of this record: ")
                    new.set_name(name)

                #Package Name Update
                print("Package Name : %s" %(new.get_packname()))
                upd = update_input(valid, "Would you like to update the Package Name?(Y/N) ")
                if upd == "Y":
                    while valid:
                        addmenu()
                        package = input("\nChoose 1 of the packages: ")
                        try:
                            package = int(package)
                            if package > 4 or package < 1:
                                print("Please enter a valid option")
                            else:
                                break
                        except:
                            print("Please enter a valid option")
            
                    package = get_packs_index(package)
                    new.set_packname(package)
                    update = 1

                #Pax Number Update
                print("Pax Number : %d" %(new.get_paxnum()))
                upd = update_input(valid, "Would you like to update the Pax Number?(Y/N) ")
                if upd == "Y":
                    while valid:
                        try:
                            paxnum = int(input("\nHow many people?: "))
                            update = 1
                            break
                        except:
                            print("Please enter a valid number")
                    
                    new.set_paxnum(paxnum)

                #Cost Per Pax Update
                if update:
                    packcost = get_packs_cost(package, new.get_paxnum())
                    print("\n== There has been an update that affects the Cost per pax ==\n")
                    print("New Cost Per Pax : %.2f" %(packcost))
                    new.set_packcost(packcost)
                else:
                    print("Current Cost Per Pax : %.2f" %(new.get_packcost()))
                
                
                print("Updating Records...")
                db[num-1] = new
                rewrite_pickles(db)

                continue

            #Delete Certain Record
            elif choice == 3:

                display_records(db)

                valid = 1
                while valid:
                    try:
                        num = int(input("Which record would you like to delete? "))
                        if num > len(db):
                            print("Please enter an EXISTING record")
                        else:
                            break
                    except:
                        print("Please enter a valid number")

                upd = update_input(valid, "Are you sure?(Y/N) ")
                if upd == "Y":
                    db.pop(num-1)
                    rewrite_pickles(db)
                else:
                    print("Returning to main menu...")

                continue
        
        #Hi cher
        elif choice == "EasterEgg":
            display_records(db)

            valid = 1
            choice = inputValue("What would you like to do? ", valid, menu(5.1))


            if choice == 1:
                display_records(db)
                valid = 1
                choice = inputValue("What would you like to do? ", valid, menu(6))

                #Bogo Sort
                if choice == 1:
                    valid = 1
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue
                    try:
                        bogoSort(db,choice)
                    except (KeyboardInterrupt):
                        print("Took too long to Sort. Welcome to O(Infinity)")
                
                elif choice == 2:
                    valid = 1
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue
                
                    stalinSort(db, choice)
                    display_records(db)
                
                elif choice == 3:
                    valid = 1
                    asc = inputValue("Ascending or Descending? ", valid, menu("asc"))
                    if asc == "X":
                        continue
                    choice = inputValue("What would you like to sort by? ",valid, menu(3))
                    if choice == "X":
                        continue
                        
                    slow_sort(db, 0 , len(db)-1, choice, asc)
                    rewrite_pickles(db)



if __name__ == "__main__":
    main()