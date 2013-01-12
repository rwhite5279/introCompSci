"""shopping_list-whiter.py , by Richard White, 2011-04-18

This program uses an external file to keep track of a shopping list. Users should be able to 1. Add to the list, 2. View the list, 3. Delete from the list, and 4. Clear the list.
"""










































































"""
PSEUDOCODE

def open_list():
    open up external file for reading
    reading in lines of items into local list
    return list to main program

def add_item():
    get item to be added
    append it to local list

def see_list():
    for list:
    print items

def delete_item():
    call see_list so they can see all the items
    ask them which item they want to remove
    pop it from list

def clear_list():
    replace list with empty list

def quit():
    write local list to external file

def main()
    open_list
    repeat
        get_choice()
    until done
    quit()
"""









































































def open_list():
    shopping_list = []
    try:
        infile = open("shopping_list.txt", "r")
        for line in infile:
            shopping_list.append(line.rstrip())
        infile.close()
    except IOError:
        print "Data file 'shopping_list.txt' not found."
        print "Starting with empty shopping list."
    return shopping_list

def add_item(shopping_list):
    new_item = raw_input("Enter new item to add to shopping list:")
    if new_item != "":
        shopping_list.append(new_item)

def see_list(shopping_list):
    for i in range(len(shopping_list)):
        print "#%3d - %-20s" % (i+1, shopping_list[i])

def delete_item(shopping_list):
    see_list(shopping_list)
    choice = input("Which item would you like to delete?: ")
    print "REALLY delete #%3d - %0s (Y/n)?" % (choice, shopping_list[choice-1]),
    confirm = raw_input().upper()
    if confirm == "Y":
        shopping_list.pop(choice-1)
        print "Item successfully deleted from list"
    else:
        print "Cancelling delete"

def clear_list(shopping_list):
    confirm = raw_input("REALLY clear entire list? (Y/n)?").upper() 
    if confirm == "Y":
        # Note that 'shopping_list = []' does NOT clear the list!
        shopping_list[:] = []
        print "Shopping list is now empty."
    else:
        print "Shopping list has been left intact."
    
def quit(shopping_list):
    print "Thank you for using the shopping list!"
    outfile = open("shopping_list.txt", "w")
    for item in shopping_list:
        outfile.write(item + "\n")
    outfile.close()

def get_choice(shopping_list):
    print "Richard's Shopping List!"
    done = False
    while not done:
        choice = ''
        while choice not in ['A','D','S','C','Q']:
            choice = raw_input("[A]dd, [D]elete Item, [S]ee List, [C]lear all, [Q]uit:").upper()
            if choice == 'A': add_item(shopping_list)
            elif choice == 'D': delete_item(shopping_list)
            elif choice == 'S': see_list(shopping_list)
            elif choice == 'C': clear_list(shopping_list)
            elif choice == 'Q': 
                quit(shopping_list)
                done = True
                break

def main():
    shopping_list = open_list()
    get_choice(shopping_list)

if __name__ == "__main__":
    main()
