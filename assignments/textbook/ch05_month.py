# month.py, Chapter 4, Example
# From Zelle's Python Programming, Chapter 4
# A program to print the abbreviation of a month, given its number

def main():
    months_string = "JanFebMarAprMayJunJulAugSepOctNovDec"
    month_num = input ("Which month would you like to see? (Enter 1-12):")

    # Once we know what number they want, get the correct segment of the string
    # to display by slicing it.
    # Note that month 1 goes from 0-2, month 2 goes from 3-5, etc.

    initial_position = (month_num-1)*3

    # Note that when we "slice" (using square brackets [i:j]), we go up to
    # BUT NOT INCLUDING the character at position j.

    desired_month = months_string[initial_position:initial_position+3]
    print "The abbrevation for month number",month_num,"is",desired_month + "!"

main()


