
from records import Records
from general.functions import *
from tree.binarysearchtree import *
from sorting.slowsortingfuncs import *

#Extras to be done : Design (Color Codes)

#Functions to be done : Table Algorithm, must be useful (so check for time complexity), Do the return to previous page, Fix up UI

#Search Funcs: https://stackabuse.com/search-algorithms-in-python/
#Possible :

#Maybe Functions : CubeSort O(n log n)

#Fun Functions : Bogo Sort / Bozo Sort : o(infinity), slow sort, sleep sort, stalin sort, bogo search

#Dropped, Why : RaditzSort (Only good time complexity when large amount of data), shell sort (overall bad time complexity), Intrapolation Search (No use of implementation),  Tim Sort, Intra Sort, (Involves merge / quick / insertion no extra marks involved, probably have but not as much as new algoritms)

#Done: All Basic Features to get a passing grade, Counting Sort, Additonal Features for administrators (Add, Remove, Update), Jump Search, Exponential Search, Shell Sort, Gnome Sort, comb sort, cocktail shaker sort. Binary Tree Search, Tree Sort, Fibo search (Single Occurence), Heap Sort, Fibonnachi Search, Binary Search Tree, Pancake Sort


def main():
    choice = ''
    while (choice != 'X'):
        db = open_pickles()
        logs = menu(1)
        while (True):
            choice = input("\u001b[7m What would you like to do? \u001b[0m ")
            try: 
                choice = int(choice)
                if (choice not in logs):
                    print("Please enter either a valid option")
                else:
                    print(logs[choice])
                    break

            except:
                if (choice.upper() in logs):
                    print(logs[choice.upper()])
                    return choice.upper()
                else:
                    print("Please enter a valid option")
        
        if (choice == 1):
            display_records(db)
            valid = 1
            secChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(5))

            #To Sort
            if (secChoice == 1):
                display_records(db)
                tertChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(2))
                if tertChoice != 'X':
                    sorting(db, valid, tertChoice)

            #To Search
            if (secChoice == 2):
                display_records(db)
                tertChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(2.1))
                if tertChoice != 'X':
                    search(db,tertChoice)

            #To List
            if (secChoice == 3):
                display_records(db)
                tertChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(2.2))
                if (tertChoice == 1):
                    listBy = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu("list"))
                    if (listBy != "X"):
                        listingFunc(db,valid,listBy)

        elif (choice == 2):
            valid = 1
            secChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(1.1))

            #Adding a Record
            if (secChoice == 1):
                obj = Records()
                name = input("Name: ")
                while (valid):
                    addmenu()
                    try:
                        package = int(input("\u001b[7m Choose One Of the Packages: \u001b[0m "))
                        if (1 > package) or (package > 4):
                            print("Please enter a valid option")
                        else:
                            break
                    except:
                        print("Please enter a valid option")
                
                package = get_packs_index(package)

                while (valid):
                    try:
                        paxnum = int(input("\u001b[7m How many people: \u001b[0m "))
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
        
            #Update Record
            elif (secChoice == 2):
                display_records(db)

                update = 0
                valid = 1
                while (valid):
                    try:
                        num = int(input("\u001b[7m Which record would you like to update? \u001b[0m "))
                        if (num > len(db)):
                            print("Please enter an EXISTING record")
                        else:
                            break
                    except:
                        print("Please enter a valid number")

                new = db[num-1]

                #Name Update
                print("Name : %s" %(new.get_name()))
                upd = update_input(valid, "\u001b[7m Would you like to update the Name?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    name = input("Enter the new name of this record: ")
                    new.set_name(name)

                #Package Name Update
                print("Package Name : %s" %(new.get_packname()))
                upd = update_input(valid, "\u001b[7m Would you like to update the Package Name?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    while (valid):
                        addmenu()
                        try:
                            package = int(input("\u001b[7m Choose one of the Packages: \u001b[0m "))
                            if (package > 4) or (package < 1):
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
                upd = update_input(valid, "\u001b[7m Would you like to update the Pax Number?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    while (valid):
                        try:
                            paxnum = int(input("\u001b[7m How many people? \u001b[0m "))
                            break
                        except:
                            print("Please enter a valid number")
                    
                    update = 1
                    package = new.get_packname()
                    new.set_paxnum(paxnum)

                #Cost Per Pax Update
                if (update):
                    packcost = get_packs_cost(package, new.get_paxnum())
                    print("== There has been an update that affects the Cost per pax ==")
                    print("New Cost Per Pax : %.2f" %(packcost))
                    new.set_packcost(packcost)
                else:
                    print("Current Cost Per Pax : %.2f" %(new.get_packcost()))
                
                
                print("Updating Records...")
                db[num-1] = new
                rewrite_pickles(db)

            #Delete Certain Record
            elif (secChoice == 3):
                display_records(db)
                valid = 1
                while (valid):
                    try:
                        num = int(input("\u001b[7m Which record would you like to update? \u001b[0m "))
                        if (num > len(db)):
                            print("Please enter an EXISTING record")
                        else:
                            break
                    except:
                        print("Please enter a valid number")

                upd = update_input(valid, "\u001b[7m Are you sure?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    db.pop(num-1)
                    rewrite_pickles(db)
                else:
                    print("Returning to main menu...")

        elif (choice == "EasterEgg"):
            display_records(db)
            valid = 1
            secChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(5.1))
            if (secChoice == 1):
                display_records(db)
                tertChoice = inputValue("\u001b[7m What would you like to do? \u001b[0m ", valid, menu(6))
                if tertChoice != 'X':
                    slow_sorting(db, valid, tertChoice)

if __name__ == "__main__":
    main()