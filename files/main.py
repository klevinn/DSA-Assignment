
from records import Records
from general.functions import *
from tree.binarysearchtree import *
from sorting.slowsortingfuncs import *

"""
Comments

Done Functions;
- All Required Functions
- Advanced Sorts
    -Counting Sort Function
    -Shell Sort Function
    -Comb Sort Function
    -Heap Sort Function
    -Pancake Sort Function
    -Tree Sort Function
    -Gnome Sort Function
    -Stalin Sort Function
    -Bozo Sort Function
    -Sleep Sort Function
    -Slow Sort Function
    -Cocktail Shaker Sort Function
- Advanced Search (https://stackabuse.com/search-algorithms-in-python/)
    -Jump Search Function
    -Exponential Search Function
    -Binary Tree Search Function
    -Fibonacci Search Function
- Additional Features for Admins
    - Add Record Function
    - Delete Record Function
    - Update Record Function
- Extras 
    - UI (Coloring)
- Dropped Features
    -Raditz Sort.
        -Only good time complexity for large amount of data
    -Interpolation Search.
        -Similar to another search function (No use of implementation)
    -Tim Sort.
        -Algorithm for .sort() in Python
        -Involves Searches Learnt in Syllabus (Merely just combining the two)
    -Intro Sort
        -Involves Searches Learnt in Syllabus (Merely just combining the two)

Error Handling :
All menus - Disallow any input that is not an available option
All sorts - Ascending & Descending Function Works
All Search - Properly Working
"""

def main():
    choice = ''
    while (choice != 'X') and (choice != 'x'):
        db = open_pickles()
        logs = menu(1)
        while (True):
            choice = input("\u001b[7mWhat would you like to do? \u001b[0m ")
            try: 
                choice = int(choice)
                if (choice not in logs):
                    print("\n\u001b[31mPlease enter either a valid option\u001b[0m\n")
                else:
                    print(logs[choice])
                    break

            except:
                if (choice.upper() in logs):
                    print(logs[choice.upper()])
                    break
                else:
                    print("\n\u001b[31mPlease enter a valid option\u001b[0m\n")
        
        if (choice == 1):
            display_records(db)
            valid = 1
            secChoice = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(5))

            #To Sort
            if (secChoice == 1):
                display_records(db)
                tertChoice = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(2))
                if tertChoice != 'X':
                    sorting(db, valid, tertChoice)

            #To Search
            if (secChoice == 2):
                display_records(db)
                tertChoice = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(2.1))
                if tertChoice != 'X':
                    search(db,tertChoice)

            #To List
            if (secChoice == 3):
                display_records(db)
                tertChoice = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(2.2))
                if (tertChoice == 1):
                    listBy = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu("list"))
                    if (listBy != "X"):
                        listingFunc(db,valid,listBy)

        elif (choice == 2):
            valid = 1
            secChoice = inputValue("\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(1.1))

            #Adding a Record
            if (secChoice == 1):
                obj = Records()
                name = input("\n\u001b[7mName:\u001b[0m ")
                while (valid):
                    addmenu()
                    try:
                        package = int(input("\n\u001b[7mChoose One Of the Packages: \u001b[0m "))
                        if (1 > package) or (package > 4):
                            print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")
                        else:
                            break
                    except:
                        print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")
                
                package = get_packs_index(package)

                while (valid):
                    try:
                        paxnum = int(input("\n\u001b[7mHow many people: \u001b[0m "))
                        break
                    except:
                        print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")

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
                        num = int(input("\n\u001b[7mWhich record would you like to update? \u001b[0m "))
                        if (num > len(db)):
                            print("\n\u001b[31mPlease enter an EXISTING record \u001b[0m\n ")
                        else:
                            break
                    except:
                        print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")

                new = db[num-1]

                #Name Update
                print("\n\u001b[1mName : %s\u001b[0m" %(new.get_name()))
                upd = update_input(valid, "\n\u001b[7mWould you like to update the Name?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    name = input("\n\u001b[7mEnter the new name of this record: \u001b[0m")
                    new.set_name(name)

                #Package Name Update
                print("\n\u001b[1mPackage Name : %s\u001b[0m" %(new.get_packname()))
                upd = update_input(valid, "\n\u001b[7mWould you like to update the Package Name?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    while (valid):
                        addmenu()
                        try:
                            package = int(input("\n\u001b[7mChoose one of the Packages: \u001b[0m "))
                            if (package > 4) or (package < 1):
                                print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")
                            else:
                                break
                        except:
                            print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")
            
                    package = get_packs_index(package)
                    new.set_packname(package)
                    update = 1

                #Pax Number Update
                print("\n\u001b[1mPax Number : %d\u001b[0m" %(new.get_paxnum()))
                upd = update_input(valid, "\n\u001b[7mWould you like to update the Pax Number?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    while (valid):
                        try:
                            paxnum = int(input("\n\u001b[7mHow many people? \u001b[0m "))
                            break
                        except:
                            print("\n\u001b[31mPlease enter a valid option \u001b[0m\n ")
                    
                    update = 1
                    package = new.get_packname()
                    new.set_paxnum(paxnum)

                #Cost Per Pax Update
                if (update):
                    packcost = get_packs_cost(package, new.get_paxnum())
                    print("\n\u001b[33m== There has been an update that affects the Cost per pax ==\u001b[0m")
                    print("\u001b[33mNew Cost Per Pax : %.2f\u001b[0m" %(packcost))
                    new.set_packcost(packcost)
                else:
                    print("\n\u001b[33mCurrent Cost Per Pax : %.2f\u001b[0m" %(new.get_packcost()))
                
                
                print("\n\u001b[33mUpdating Records...\u001b[0m")
                db[num-1] = new
                rewrite_pickles(db)

            #Delete Certain Record
            elif (secChoice == 3):
                display_records(db)
                valid = 1
                while (valid):
                    try:
                        num = int(input("\n\u001b[7mWhich record would you like to delete? \u001b[0m "))
                        if (num > len(db)):
                            print("\n\u001b[31mPlease enter an EXISTING record\u001b[0m\n")
                        else:
                            break
                    except:
                        print("\n\u001b[31mPlease enter a valid number\u001b[0m\n")

                upd = update_input(valid, "\n\u001b[7mAre you sure?(Y/N): \u001b[0m ")
                if (upd == "Y"):
                    db.pop(num-1)
                    rewrite_pickles(db)
                else:
                    print("\n\u001b[33mReturning to main menu...\u001b[0m")

        elif (choice == "EasterEgg"):
            display_records(db)
            valid = 1
            secChoice = inputValue("\n\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(5.1))
            if (secChoice == 1):
                display_records(db)
                tertChoice = inputValue("\n\u001b[7mWhat would you like to do? \u001b[0m ", valid, menu(6))
                if tertChoice != 'X':
                    slow_sorting(db, valid, tertChoice)

if __name__ == "__main__":
    main()