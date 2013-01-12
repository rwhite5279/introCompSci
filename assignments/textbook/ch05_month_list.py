# month_list.py, Chapter 4, Example
# From Zelle's Python Programming, Chapter 4
# A program to print the abbreviation of a month, given its number

def main():
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_num = input ("Which month would you like to see? (Enter 1-12):")

    # Once we know what number they want, get the correct element of the list
    # (This means we have to subtract one from the number they gave us, because
    # the list starts at 0!)

    desired_month = months_list[month_num - 1]

    print "The name of month number",month_num,"is",desired_month + "!"

main()


